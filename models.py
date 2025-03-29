'''zxc'''
from typing import List
from peewee import MySQLDatabase, Model, CharField, ForeignKeyField

mysql_db = MySQLDatabase('db_bb', user='root', password='1234',
                         host='127.0.0.1', port=3306)


class BaseModel(Model):
    '''zxc'''
    class Meta:
        '''zxc'''
        database = mysql_db


class User(BaseModel):
    '''zxc'''
    username = CharField()
    name = CharField()
    password = CharField()
    link_tg = CharField()


class Role(BaseModel):
    '''zxc'''
    name = CharField()


class UserRole(BaseModel):
    '''zxc'''
    user = ForeignKeyField(User)
    role = ForeignKeyField(Role)


if __name__ == '__main__':
    mysql_db.connect()
    mysql_db.create_tables([User, Role, UserRole])


# user = User.get_or_none(username='user3')
# user_roles: List[UserRole] = (
#     UserRole
#     .select(User.username, Role.name)
#     .join(User, on=(UserRole.user == User.id))
#     .join(Role, on=(UserRole.role == Role.id))
#     .where(UserRole.user == user)
# )

# for user_role in user_roles.dicts():
#     print(user_role['username'], user_role['name'])
