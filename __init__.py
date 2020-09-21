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


if module == "getDatabases":
    result = GetParams("result")

    try:
        database_names = client.database_names()
        SetVar(result, database_names)
    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "getCollections":
    database = GetParams("db")
    result = GetParams("result")

    try:
        collections = client[database].list_collection_names()
        SetVar(result, collections)
    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e
    
if module == "getDocuments":
    database = GetParams("db")
    collection = GetParams("collection")
    result = GetParams("result")

    try:
        collection = client[database][collection]
        documents = []
        for document in collection.find():
            doc = {key: str(value) for key, value in document.items()}
            documents.append(doc)

        SetVar(result, documents)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "createCollection":
    database = GetParams("db")
    collection = GetParams("collection")

    try:
        client[database].create_collection(collection)
    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
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
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
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
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
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
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "findAndReplace":
    database = GetParams("db")
    collection = GetParams("collection")
    id_ = GetParams("id")
    new_document = GetParams("new")
    result = GetParams("result")

    try:

        collection = client[database][collection]
        new_document = eval(new_document)
        doc = collection.find_one_and_update({"_id": ObjectId(id_)}, {'$set': new_document})
        response = True if doc else False

        SetVar(result, response)

    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e

    
    




