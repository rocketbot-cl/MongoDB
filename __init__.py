# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'MongoDB' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)

from pymongo import MongoClient
import pymongo
from bson import ObjectId


"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")
global client

if module == "connect":
    url = GetParams('url')
    client = MongoClient(url)
    
    db = client.test
    print(dir(db.prueba))

if module == "getDatabases":
    result = GetParams("result")

    try:
        database_names = client.database_names()
        SetVar(result, database_names)
    except Exception as e:
        PrintException()
        raise e

if module == "getCollections":
    database = GetParams("db")
    result = GetParams("result")

    try:
        collections = client[database].list_collection_names()
        SetVar(result, collections)
    except Exception as e:
        PrintException()
        raise e
    
if module == "getDocuments":
    database = GetParams("db")
    collection = GetParams("collection")
    result = GetParams("result")

    try:
        collection = client[database][collection]
        documents = [dict(document.items()) for document in collection.find()]
        SetVar(result, documents)
    except Exception as e:
        PrintException()
        raise e

if module == "createCollection":
    database = GetParams("db")
    collection = GetParams("collection")

    try:
        client[database].create_collection(collection)
    except Exception as e:
        PrintException()
        raise e

if module == "createDocument":
    database = GetParams("db")
    collection = GetParams("collection")
    doc = GetParams("doc")
    result = GetParams("result")

    try:
        doc = eval(doc)
        doc_id = client[database][collection].insert_one(doc).inserted_id
        SetVar(result, doc_id)

    except Exception as e:
        PrintException()
        raise e

if module == "findById":
    database = GetParams("db")
    collection = GetParams("collection")
    id_ = GetParams("id")
    result = GetParams("result")

    try:

        collection = client[database][collection]
        doc = collection.find_one({"_id": ObjectId(id_)})
        doc = dict(doc.items())

        SetVar(result, doc)

    except Exception as e:
        PrintException()
        raise e

if module == "find":
    database = GetParams("db")
    collection = GetParams("collection")
    dic = GetParams("dict")
    result = GetParams("result")

    try:
        dic = eval(dic)
        collection = client[database][collection]
        docs = collection.find(dic)
        documents = [dict(doc.items()) for doc in docs]

        SetVar(result, documents)

    except Exception as e:
        PrintException()
        raise e
    
    
    



