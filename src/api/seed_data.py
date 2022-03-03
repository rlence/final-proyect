from api.shared.encrypte_pass import encryp_pass
import datetime


data = {
    "User":[
        {
            "id": 1,
            "name": 'Raquel',
            "last_name": 'García',
            "email": 'raquelgarciatrives@gmail.com',
            "password": encryp_pass('123')
        },
         {
            "id": 2,
            "name": 'Eva',
            "last_name": 'Naranjo',
            "email": 'evita.naranjo@gmail.com',
            "password": encryp_pass('1234')
        }
    ],
    "Ingredient":[
        {
            "id": 1,
            "name": 'Espinacas'
        },
        {
            "id": 2,
            "name": 'Pollo' 
        },
        {
            "id": 3,
            "name": 'Tofu'
        }
         
    ],
    "Recipe":[
        {
            "id": 1,
            "photo": "",
            "title": "Salmón marinado a baja temperatura",
            "description": "salmoncito rico marinado con limon, soja, pimienta negra ",
            "private": True,
            "tag": 0,
            "id_user": 1,
            
        },
        {
            "id": 2,
            "photo": "",
            "title": "Arroz abanda",
            "description": "Sofrito de verduras, incorporar calamar, majado con ñora, ajo tostado y azafrán. Añadir fumet de moralla y arroz, sofreir 3 minutos, incorporar gambas y a darle al fuego!!!! ",
            "private": False,
            "tag": 1,
            "id_user": 2,
            
        },
        {
            "id": 3,
            "photo": "",
            "title": "Pollo al marsala/oporto",
            "description": "pechuga de pollo sofreir enharinada con orégano a fuego fuerte, reservar. Freir ajo laminado, incorporar champiñones , un vaso de oporto. Reducir a fuergo fuerte. Incorporar un vaso de caldo de pollo y las pechugas. Dejar cocer 5 minutos",
            "private": True,
            "tag": 2,
            "id_user": 1,
        },
    ],
    "Menu":[
        {
            "id": 1,
            "title": "Menus ligth",
            "create_at": datetime.datetime.now(),
            "id_user": 1,

        },
        {
            "id": 2,
            "title": "Menus niños",
            "create_at":  datetime.datetime.now(),
            "id_user": 2,

        },
        {
            "id": 3,
            "title": "Menu verano",
            "create_at": datetime.datetime.now(),
            "id_user": 1,

        }

    ],
    "Recipe_menu":[
        {
            "id": 1,
            "id_menu":1,
            "id_recipe": 1,
            
        },
        {
            "id": 2,
            "id_menu": 1,
            "id_recipe": 2,
            
        },
        {
            "id": 3,
            "id_menu": 2,
            "id_recipe": 3,
            
        },
        {
            "id": 4,
            "id_menu": 2,
            "id_recipe": 1,
            
        },
        {
            "id": 5,
            "id_menu": 3,
            "id_recipe": 2,
            
        },
    ],
    "Recipe_ingredient":[
        {
            "id": 1,
            "quantity": 200,
            "id_ingredient": 1,
            "id_recipe": 1,
            
        },
         {
            "id": 2,
            "quantity": 100,
            "id_ingredient": 1,
            "id_recipe": 2,
            
        },
         {
            "id": 3,
            "quantity": 30,
            "id_ingredient": 3,
            "id_recipe": 2,
            
        },
         {
            "id": 4, 
            "quantity": 70,
            "id_ingredient": 1,
            "id_recipe": 3,
            
        }

    ]
}