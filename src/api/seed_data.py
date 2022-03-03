
from api.shared.encryp_pass import encryp_pass

data = {
    "User":[
        {
            
            "name": 'Raquel',
            "last_name": 'García',
            "email": 'raquelgarciatrives@gmail.com',
            "password": encryp_pass('123')
        },
         {
           
            "name": 'Eva',
            "last_name": 'Naranjo',
            "email": 'evita.naranjo@gmail.com',
            "password": encryp_pass('1234')
        }
    ],
    "Ingredient":[
        {
            
            "name": 'Espinacas'
        },
        {
            
            "name": 'Pollo' 
        },
        {
            
            "name": 'Tofu'
        }
         
    ],
    "Recipe":[
        {
            "photo": "",
            "title": "Salmón marinado a baja temperatura",
            "description": "salmoncito rico marinado con limon, soja, pimienta negra ",
            "private": True,
            "tag": 0,
            "id_user": 1,
            
        },
        {
            "photo": "",
            "title": "Arroz abanda",
            "description": "Sofrito de verduras, incorporar calamar, majado con ñora, ajo tostado y azafrán. Añadir fumet de moralla y arroz, sofreir 3 minutos, incorporar gambas y a darle al fuego!!!! ",
            "private": False,
            "tag": 1,
            "id_user": 2,
            
        },
        {
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
            "title": "Menus ligth",
            "create_at": self.create,
            "id_user": 1,

        },
        {
            "title": "Menus niños",
            "create_at": self.create,
            "id_user": 2,

        },
        {
            "title": "Menu verano",
            "create_at": self.create,
            "id_user": 1,

        }

    ],
    "Recipe_menu":[
        {
             "id_menu":1,
            "id_recipe": 1,
            
        },
        {
             "id_menu": 1,
            "id_recipe": 2,
            
        },
        {
             "id_menu": 2,
            "id_recipe": 3,
            
        },
        {
             "id_menu": 2,
            "id_recipe": 1,
            
        },
        {
             "id_menu": 3,
            "id_recipe": 2,
            
        },
    ],
    "Recipe_ingredient":[
        {
            "quantity": 200,
            "id_ingredient": 1,
            "id_recipe": 1,
            
        },
         {
            "quantity": 100,
            "id_ingredient": 1,
            "id_recipe": 2,
            
        },
         {
            "quantity": 30,
            "id_ingredient": 3,
            "id_recipe": 2,
            
        },
         {
            "quantity": 70,
            "id_ingredient": 1,
            "id_recipe": 3,
            
        }

    ]
}