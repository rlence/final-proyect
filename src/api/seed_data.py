from api.shared.encrypte_pass import encryp_pass
import datetime


data = {
    "User":[
        {
            "id": 1000001,
            "name": 'Raquel',
            "last_name": 'García',
            "email": 'raquelgarciatrives@gmail.com',
            "password": encryp_pass('123')
        },
         {
            "id": 1000002,
            "name": 'Eva',
            "last_name": 'Naranjo',
            "email": 'evita.naranjo@gmail.com',
            "password": encryp_pass('1234')
        }
    ],
    "Ingredient":[
        {
            "id": 1000001,
            "name": 'Espinacas'
        },
        {
            "id": 1000002,
            "name": 'Pollo' 
        },
        {
            "id": 1000003,
            "name": 'Tofu'
        }
         
    ],
    "Recipe":[
        {
            "id": 10000001,
            "photo": "",
            "title": "Salmón marinado a baja temperatura",
            "description": "salmoncito rico marinado con limon, soja, pimienta negra ",
            "private": True,
            "tag": 0,
            "id_user": 1000001,
            
        },
        {
            "id": 10000002,
            "photo": "",
            "title": "Arroz abanda",
            "description": "Sofrito de verduras, incorporar calamar, majado con ñora, ajo tostado y azafrán. Añadir fumet de moralla y arroz, sofreir 3 minutos, incorporar gambas y a darle al fuego!!!! ",
            "private": False,
            "tag": 1,
            "id_user": 1000002,
            
        },
        {
            "id": 10000003,
            "photo": "",
            "title": "Pollo al marsala/oporto",
            "description": "pechuga de pollo sofreir enharinada con orégano a fuego fuerte, reservar. Freir ajo laminado, incorporar champiñones , un vaso de oporto. Reducir a fuergo fuerte. Incorporar un vaso de caldo de pollo y las pechugas. Dejar cocer 5 minutos",
            "private": True,
            "tag": 2,
            "id_user": 1000001,
        },
    ],
    "Menu":[
        {
            "id": 10000001,
            "title": "Menus ligth",
            "create_at": datetime.datetime.now(),
            "id_user": 1000001,

        },
        {
            "id": 10000002,
            "title": "Menus niños",
            "create_at":  datetime.datetime.now(),
            "id_user": 1000002,

        },
        {
            "id": 10000003,
            "title": "Menu verano",
            "create_at": datetime.datetime.now(),
            "id_user": 1000001,

        }

    ],
    "Recipe_menu":[
        {
            "id": 1000001,
            "id_menu":10000001,
            "id_recipe": 10000001,
            
        },
        {
            "id": 1000002,
            "id_menu": 10000002,
            "id_recipe": 10000002,
            
        },
        {
            "id": 1000003,
            "id_menu": 10000002,
            "id_recipe": 10000003,
            
        },
        {
            "id": 1000004,
            "id_menu": 10000003,
            "id_recipe":10000001,
            
        },
        {
            "id": 1000005,
            "id_menu": 10000003,
            "id_recipe": 10000002,
            
        },
    ],
    "Recipe_ingredient":[
        {
            "id": 1000000,
            "quantity": 200,
            "id_ingredient": 1000001,
            "id_recipe": 10000001,
            
        },
         {
            "id": 2000000,
            "quantity": 100,
            "id_ingredient": 1000001,
            "id_recipe":  10000002,
            
        },
         {
            "id": 3000000,
            "quantity": 30,
            "id_ingredient": 1000003,
            "id_recipe":  10000002,
            
        },
         {
            "id": 4000000, 
            "quantity": 70,
            "id_ingredient": 1000001,
            "id_recipe": 10000003,
            
        }

    ]
}