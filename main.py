from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.responses import RedirectResponse


#validation
class student(BaseModel):
    name : str
    age  : int
    gender  : str
    marks  : int
    course  : str
    image  : str
    status  : int 



import sqlite3
def get_connection():
    connection=sqlite3.connect(
        "students.db"
    )
    return connection

get_connection()

def create_table():
    connection=get_connection()
    cursor=connection.cursor()
    q="""create table IF not EXISTS students(id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    marks INTEGER,
    course TEXT,
    image TEXT,status INTEGER)"""
    cursor.execute(q)
    connection.commit()
    connection.close()

create_table()


app=FastAPI()
templates=Jinja2Templates(
    directory="templates"
)


@app.get("/")
def home_page(req:Request):
    connection=get_connection()
    cursor=connection.cursor()
    q="select * from students"
    cursor.execute(q)
    students=cursor.fetchall()
    connection.close()
    return templates.TemplateResponse(
        request=req,
        name="home.html",
        context={"st":students}
    )

@app.get("/students/add")
def std_add(req:Request):
    return templates.TemplateResponse(
        request=req,
        name="add.html",
        context={}
    )

@app.post("/students/add")
def create_std(name=Form(),age=Form(),gender=Form(),marks=Form(),course=Form(),image=Form(),status=Form()):
    
#validation
    std=student(
        name = name,
        age  = age,
        gender = gender,
        marks  = marks,
        course  = course,
        image  = image,
        status  = status,        
    )
    values=(std.name,std.age,std.gender,std.marks,std.course,std.image,std.status)


    connection=get_connection()
    cursor=connection.cursor()
    q="""insert into students(name,age,gender,marks,course,image,status) 
    values(?,?,?,?,?,?,?)"""
    cursor.execute(q,values)
    connection.commit()
    connection.close()

    return RedirectResponse(url="/",status_code=303)


@app.get("/students/{std_id}")
def sing_std(req:Request,std_id:int):
    connection=get_connection()
    cursor=connection.cursor()
    q="select * from students where id=?"
    cursor.execute(q,(std_id,))
    student=cursor.fetchone()
    connection.close()
    return templates.TemplateResponse(
        request=req,
        name="std.html",
        context={"std":student}
    )

@app.post("/students/del/{std_id}")
def sing_std(req:Request,std_id:int):
    connection=get_connection()
    cursor=connection.cursor()
    q="delete from students where id=?"
    cursor.execute(q,(std_id,))
    connection.commit()
    connection.close()

    return RedirectResponse(url="/",status_code=303)

@app.get("/students/edit/{std_id}")
def edit (req:Request,std_id:int):
    connection=get_connection()
    cursor=connection.cursor()
    q="select *  from students where id=?"
    cursor.execute(q,(std_id,))
    student=cursor.fetchone()
    return templates.TemplateResponse(
        request=req,
        name="edit.html",
        context={"std":student}
    )

@app.post("/student/edit/{std_id}")
def sing_std(std_id:int,name=Form(),age=Form(),gender=Form(),marks=Form(),course=Form(),image=Form(),status=Form()):
    std=student(name = name,
                age  = age,
                gender = gender,
                marks  = marks,
                course  = course,
                image  = image,
                status  = status,        
                )  
    connection=get_connection()
    cursor=connection.cursor()
    q="""update students set name=?,age=?,gender=?,marks=?,course=?,image=?,status=? where id=?"""
    cursor.execute(q,(std.name,std.age,std.gender,std.marks,std.course,std.image,std.status,std_id,))
    connection.commit()
    connection.close()

    return RedirectResponse(url="/",status_code=303)

# to reset the auto increment
# def reset_ids():
#     connection = get_connection()
#     cursor = connection.cursor()

#     cursor.execute("UPDATE students SET id=2 WHERE id=10")

#     cursor.execute("""
#         UPDATE sqlite_sequence
#         SET seq=2
#         WHERE name='students'
#     """)

#     connection.commit()
#     connection.close()

# reset_ids()