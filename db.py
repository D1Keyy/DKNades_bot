import sqlite3

db=sqlite3.connect('database.db')
cursor=db.cursor()
async def getmessagetext(messageid):
    try:
        cursor.execute(f'SELECT text_message FROM messages WHERE id={messageid}')
        text=cursor.fetchone()
        return text
    except Exception as e:
        print(e)