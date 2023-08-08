from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
import openpyxl
from sqlalchemy import create_engine

from excel_api.serializers import MyModelSerializer
from .models import ExcelFile, MyModel
import pandas as pd

engine = create_engine("sqlite:///C:\\path\\to\\foo.db")
# Create your views here.
@api_view(['POST'])
def index(request):
    file = request.FILES['files']
    obj = ExcelFile.objects.create(
        file = file
    )
    path = str(obj.file)
    df = pd.read_excel(path)
    """for d in df.values:
        try:
            if not MyModel.objects.get(id=d[0]):
                pass
        except MyModel.DoesNotExist:
           MyModel.objects.create(
                    id=d[0],
                    name=d[1],
                    type=d[2],
                    sub_type=d[3],
                    new = d[4]
                )
    users = MyModel.objects.all()
    serializer = MyModelSerializer(users, many=True)"""
    df.to_sql(name='Table1', if_exists='append')
    return Response("Success")

@api_view(['GET'])
def show(request):
    users = MyModel.objects.all()
    serializer = MyModelSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update(request):
    file = request.FILES['files']
    obj = ExcelFile.objects.create(
        file = file
    )
    path = str(obj.file)
    df = pd.read_excel(path)
    for d in df.values:
        MyModel.objects.update_or_create(
                    id=d[0],
                    name=d[1],
                    type=d[2],
                    sub_type=d[3],
                    new = d[4]
                )
    users = MyModel.objects.all()
    
    serializer = MyModelSerializer(users, many=True)
    return Response(serializer.data)


class Api(APIView):
    def __init__(self):
        self.conn_default = create_engine("sqlite:///G:\\Django\\assignment1\\db.sqlite3").connect()


    
    def post(self,request):
        file = request.FILES['files']
        obj = ExcelFile.objects.create(
            file = file
        )
        path = str(obj.file)
        df = pd.read_excel(path)
        #print(df)
        df2= df
        data = pd.read_sql_query('SELECT * FROM Table3', self.conn_default)
        df2 = pd.merge(df,data)

        df2 = df2.drop_duplicates()
        print(df2)
        print(df.values)
        if df2.keys == df.keys:
            print("if")
            df2.to_sql("Table3",if_exists='append', index=False,con=self.conn_default, schema=None)
        else:
            print("else")
            df2.to_sql("Table3",if_exists='replace', index=False,con=self.conn_default, schema=None)
        return Response("Success")
    
    """ def post(self, request):
        file = request.FILES['files']
        obj = ExcelFile.objects.create(
            file = file
        )
        path = str(obj.file)
        df = pd.read_excel(path)
        df.to_sql("Table1",if_exists='append', index=False,con=self.conn_default)
        return Response("Success!")"""