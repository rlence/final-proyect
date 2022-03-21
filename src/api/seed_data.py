from api.shared.encrypte_pass import encryp_pass
import datetime


data = {
    "User":[
        {
            "id": 100000001,
            "name": 'Raquel',
            "last_name": 'García',
            "email": 'raquelgarciatrives@gmail.com',
            "password": encryp_pass('123')
        },
         {
            "id": 100000002,
            "name": 'Eva',
            "last_name": 'Naranjo',
            "email": 'evita.naranjo@gmail.com',
            "password": encryp_pass('1234')
        }
    ],
    "Ingredient":[
        {
            "id": 100,
            "name": 'Huevos'
        },
        {
            "id": 101,
            "name": 'Lenche entera'
        },
        {
            "id": 102,
            "name": 'Extracto de vainilla'
        },
        {
            "id": 103,
            "name": 'Levadura química'
        },
        {
            "id": 104,
            "name": 'Azúcar'
        },
        {
            "id": 105,
            "name": 'Espinacas'
        },
        {
            "id": 106,
            "name": 'Pollo' 
        },
        {
            "id": 107,
            "name": 'Tofu'
        },
        {
            "id": 108,
            "name": 'Harina'
        },
        {
            "id": 109,
            "name": 'Bebida de avena'
        },
        {
            "id": 110,
            "name": 'Aceite de oliva'
        },
        {
            "id": 111,
            "name": 'Calabacín'
        },
        {
            "id": 112,
            "name": 'Pimiento rojo'
        },
        {
            "id": 113,
            "name": 'Pimiento verde'
        },
        {
            "id": 114,
            "name": 'Berenjena'
        },
        {
            "id": 115,
            "name": 'Kale'
        },
        {
            "id": 116,
            "name": 'Brócoli'
        },
        {
            "id": 117,
            "name": 'Rúcula'
        },
        {
            "id": 118,
            "name": 'Lechuga romana'
        },
        {
            "id": 120,
            "name": 'Lechuga iceberg'
        },
        {
            "id": 121,
            "name": 'Escarola'
        },
        {
            "id": 122,
            "name": 'Aguacate'
        },
        {
            "id": 123,
            "name": 'Tomate'
        },
        {
            "id": 124,
            "name": 'Aceitunas verdes'
        },
        {
            "id": 125,
            "name": 'Aceitunas negras'
        },
        {
            "id": 126,
            "name": 'Cebolla'
        },
        {
            "id": 127,
            "name": 'Espárragos trigueros'
        },
        {
            "id": 128,
            "name": 'Espárragos blancos'
        },
        {
            "id": 129,
            "name": 'Patata'
        },
        {
            "id": 130,
            "name": 'Berza'
        },
        {
            "id": 131,
            "name": 'Calabaza'
        },
        {
            "id": 132,
            "name": 'Rábano'
        },
        {
            "id": 133,
            "name": 'Borraja'
        },
        {
            "id": 134,
            "name": 'Acelga'
        },
        {
            "id": 135,
            "name": 'Achicoria'
        },
        {
            "id": 136,
            "name": 'Ajo'
        },
        {
            "id": 137,
            "name": 'Apio'
        },
        {
            "id": 138,
            "name": 'Alcachofa'
        },
        {
            "id": 139,
            "name": 'Puerro'
        },
        {
            "id": 140,
            "name": 'Setas'
        },
        {
            "id": 141,
            "name": 'Pepino'
        },
        {
            "id": 142,
            "name": 'Cardo'
        },
        {
            "id": 143,
            "name": 'Hinojo'
        },
        {
            "id": 144,
            "name": 'Remolacha'
        },
        {
            "id": 145,
            "name": 'Coles de bruselas'
        },
        {
            "id": 146,
            "name": 'Coliflor'
        },
        {
            "id": 147,
            "name": 'Endibia'
        },
        {
            "id": 148,
            "name": 'Judías verdes'
        },
        {
            "id": 149,
            "name": 'Ternera de guisar'
        },
        {
            "id": 150,
            "name": 'Pechuga de pollo'
        },
        {
            "id": 151,
            "name": 'Conejo'
        },
        {
            "id": 152,
            "name": 'Entrecot de ternera'
        },
        {
            "id": 153,
            "name": 'Costillas de cerdo'
        },
        {
            "id": 154,
            "name": 'Pavo'
        },
        {
            "id": 155,
            "name": 'Lomo de cerdo'
        },
        {
            "id": 156,
            "name": 'Carne picada'
        },
        {
            "id": 157,
            "name": 'Caldo de pollo'
        },
        {
            "id": 158,
            "name": 'Caldo de carne'
        },
        {
            "id": 159,
            "name": 'Caldo de verduras'
        },
        {
            "id": 160,
            "name": 'Contramuslos de pollo'
        },
        {
            "id": 161,
            "name": 'Muslos de pollo'
        },
        {
            "id": 162,
            "name": 'Caldo de cocido'
        },
        {
            "id": 163,
            "name": 'Merluza'
        },
        {
            "id": 164,
            "name": 'Rape'
        },
        {
            "id": 165,
            "name": 'Bacalao'
        },
        {
            "id": 166,
            "name": 'Rodaballo'
        },
        {
            "id": 167,
            "name": 'Lubina'
        },
        {
            "id": 168,
            "name": 'Lenguado'
        },
        {
            "id": 169,
            "name": 'Anchoas'
        },
        {
            "id": 170,
            "name": 'Sardina'
        },
        {
            "id": 171,
            "name": 'Atún'
        },
        {
            "id": 172,
            "name": 'Trucha'
        },
        {
            "id": 173,
            "name": 'Besugo'
        },
        {
            "id": 174,
            "name": 'Dorada'
        },
        {
            "id": 175,
            "name": 'Salmón'
        },
        {
            "id": 176,
            "name": 'Naranja'
        },
        {
            "id": 177,
            "name": 'Arándanos'
        },
        {
            "id": 178,
            "name": 'Uva'
        },
        {
            "id": 179,
            "name": 'Kiwi'
        },
        {
            "id": 180,
            "name": 'Mango'
        },
        {
            "id": 181,
            "name": 'Coco'
        },
        {
            "id": 182,
            "name": 'Fresa'
        },
        {
            "id": 183,
            "name": 'Granada'
        },
        {
            "id": 184,
            "name": 'Melón'
        },
        {
            "id": 185,
            "name": 'Lima'
        },
        {
            "id": 186,
            "name": 'Limón'
        },
        {
            "id": 187,
            "name": 'Sandía'
        },
        {
            "id": 188,
            "name": 'Pomelo'
        },
        {
            "id": 189,
            "name": 'Manzana'
        },
        {
            "id": 190,
            "name": 'Mandarina'
        },
        {
            "id": 191,
            "name": 'Piña'
        },
        {
            "id": 192,
            "name": 'Melocotón'
        },
        {
            "id": 193,
            "name": 'Pasas'
        },
        {
            "id": 194,
            "name": 'Dátiles'
        },
        {
            "id": 195,
            "name": 'Membrillo'
        },
        {
            "id": 196,
            "name": 'Albahaca'
        },
        {
            "id": 197,
            "name": 'Anís estrellado'
        },
        {
            "id": 198,
            "name": 'Ajo negro'
        },
        {
            "id": 199,
            "name": 'Cardamomo'
        },
        {
            "id": 200,
            "name": 'Canela'
        },
        {
            "id": 201,
            "name": 'Cilantro'
        },
        {
            "id": 202,
            "name": 'Perejil'
        },
        {
            "id": 203,
            "name": 'Comino'
        },
        {
            "id": 204,
            "name": 'Cúrcuma'
        },
        {
            "id": 205,
            "name": 'Curry'
        },
        {
            "id": 206,
            "name": 'Chile'
        },
        {
            "id": 207,
            "name": 'Estragón'
        },
        {
            "id": 208,
            "name": 'Eneldo'
        },
        {
            "id": 209,
            "name": 'Sal'
        },
        {
            "id": 210,
            "name": 'Hierbabuena'
        },
        {
            "id": 211,
            "name": 'Jengibre'
        },
        {
            "id": 212,
            "name": 'Laurel'
        },
        {
            "id": 213,
            "name": 'Melisa'
        },
        {
            "id": 214,
            "name": 'Menta'
        },
        {
            "id": 215,
            "name": 'Mostaza'
        },
        {
            "id": 216,
            "name": 'Orégano'
        },
        {
            "id": 217,
            "name": 'Pimienta negra'
        },
        {
            "id": 218,
            "name": 'Pimienta blanca'
        },
        {
            "id": 219,
            "name": 'Romero'
        },
        {
            "id": 220,
            "name": 'Tahini'
        },
        {
            "id": 221,
            "name": 'Tomillo'
        },
        {
            "id": 222,
            "name": 'Wasabi'
        },
        {
            "id": 223,
            "name": 'Salsa de soja'
        },
        {
            "id": 224,
            "name": 'Salsa teriyaki'
        },
        {
            "id": 225,
            "name": 'Leche semidesnatada'
        },
        {
            "id": 226,
            "name": 'Leche desnatada'
        },
        {
            "id": 227,
            "name": 'Bebida de soja'
        },
        {
            "id": 228,
            "name": 'Bebida de arroz'
        },
        {
            "id": 229,
            "name": 'Maíz'
        },
        {
            "id": 230,
            "name": 'Alubias'
        },
        {
            "id": 231,
            "name": 'Habas'
        },
        {
            "id": 232,
            "name": 'Lentejas'
        },
        {
            "id": 233,
            "name": 'Garbanzos'
        },
        {
            "id": 234,
            "name": 'Fideos'
        },
        {
            "id": 235,
            "name": 'Macarrones'
        },
        {
            "id": 236,
            "name": 'Espaguetis'
        },
        {
            "id": 237,
            "name": 'Jamón serrano'
        },
        {
            "id": 238,
            "name": 'Chorizo'
        },
        {
            "id": 239,
            "name": 'Cacahuetes'
        },
        {
            "id": 240,
            "name": 'Alfalfa'
        },
        {
            "id": 241,
            "name": 'Brotes de soja'
        },
        {
            "id": 242,
            "name": 'Guisantes'
        },
        {
            "id": 243,
            "name": 'Soja'
        },
        {
            "id": 244,
            "name": 'Agua'
        },
        {
            "id": 245,
            "name": 'Gambas'
        },
        {
            "id": 246,
            "name": 'Langostinos'
        },
        {
            "id": 247,
            "name": 'Calamares'
        },
        {
            "id": 248,
            "name": 'Caldo de pescado'
        },
        {
            "id": 249,
            "name": 'Morralla'
        },
        {
            "id": 250,
            "name": 'Ñora'
        },
        {
            "id": 251,
            "name": 'Tomate triturado'
        },
        {
            "id": 252,
            "name": 'Pimiento choricero'
        },
        {
            "id": 253,
            "name": 'Arroz'
        },
        {
            "id": 254,
            "name": 'Sepia'
        },
        {
            "id": 255,
            "name": 'Azafrán'
        },
        {
            "id": 256,
            "name": 'Oporto'
        },
        {
            "id": 257,
            "name": 'Champiñones'
        },
        {
            "id": 258,
            "name": 'Nata líquida'
        },
        {
            "id": 259,
            "name": 'Zanahoria'
        },
        {
            "id": 260,
            "name": 'Tomate seco'
        },
    ],
    "Recipe":[
        {
            "id": 10000,
            "photo":"https://res.cloudinary.com/dw4npwftd/image/upload/v1647883090/crema-de-calabaza_kas6mj.jpg",
            "title":"Crema de calabaza",
            "description":"Empezamos con la calabaza. Para pelarla y cortarla introduce la calabaza entera o en varios trozos en el microondas y dale 2 o 3 minutos. Ve mirando cómo está y cuando la notes un pelín menos dura ya puedes pelarla y cortarla sin dificultad. Córtala en trozos no muy grandes. Córtale a los puerros las raíces y también la parte más verde, además de la capa más externa. Córtalos por la mitad y en rodajas o directamente en rodajas. Pela la patata y córtala en trozos. En una olla que tenga tapadera pon un poco de aceite y sal y echa los puerros, la patata y la calabaza. Cocina durante unos 10 minutos a fuego medio-bajo mientras las mueves de vez en cuando. Estarán en su punto cuando empiecen a dorarse un poco. Añade el agua junto con un poco de sal, que no llegue a cubrir del todo las verduras. Pon el fuego a temperatura alta y cuando se rompa a hervir tapa la olla, baja el fuego para que esté suave y deja que se cocine durante unos 25-30 minutos, hasta que las verduras estén tiernas. Retira la olla del fuego y tritúralo todo hasta que tenga la textura que más te guste y si lo necesitas puedes añadir más agua si te parece que está demasiado espesa. Prueba la crema de calabaza y rectifica de sal si es necesario.", 
            "private": False,
            "tag": 3,
            "id_user":100000001
        },
        {
            "id": 10001,
            "photo": "https://res.cloudinary.com/dw4npwftd/image/upload/v1647883019/Arroz_a_banda_efflwm.jpg",
            "title": "Arroz a banda",
            "description": "Lava las gambas y sécalas con papel de cocina. Lava también la sepia y córtala en trozos de bocado. Pon la paellera con el fondo cubierto de aceite a fuego medio y sofríe las gambas con un poco de sal hasta que empiecen a dorarse. Escurre y reserva. Pela y pica el diente de ajo y dóralo en la paellera junto con la sepia y un poco de sal hasta que quede tierna. Mientras tanto pela las gambas, reserva la carne y tritura las cabezas y las pieles junto con un poco de caldo para que dejen su jugo en él. Cuela el caldo, añádele más caldo hasta tener los 700 ml y ponlo en un cazo a fuego medio-bajo para que esté casi hirviendo cuando lo necesitemos para cocer el arroz. Cuando la sepia esté lista, incorpora a la paellera la salsa de tomate y la carne de pimiento choricero o el pimentón, y rehógalo todo a fuego bajo durante 5 minutos. Incorpora el arroz y revuélvelo con todos los ingredientes durante 2 minutos. Vierte el caldo de pescado ya caliente sobre él, junto con un poco de azafrán o colorante. Remueve todo un poco para que quede bien repartido por la paellera, baja el fuego al mínimo y deja que se cocine unos 20 minutos. Dejar un arroz en el punto exacto es complicado pero no imposible. Aquí va el truco que debes tener en cuenta: si al cabo de unos 18-20 minutos pruebas el arroz y ves que está prácticamente listo pero queda todavía mucho caldo, sube la temperatura del fuego para que se evapore el líquido rápidamente. Si por el contrario ya no queda líquido y el arroz sigue un poco crudo, no tienes más remedio que añadir agua (o más caldo si dispones de él), y siempre añadirlo caliente o casi hirviendo. Cuando esté casi listo, coloca las gambas por encima. Deja que repose 5 o 10 minutos, mejor cubierto con un paño de cocina o papel de aluminio y siempre en la propia paellera para que mantenga el calor.",
            "private": False,
            "tag": 1,
            "id_user": 100000001,
        },
        {
            "id": 10002,
            "photo": "https://res.cloudinary.com/dw4npwftd/image/upload/v1647883173/pollo_al_oporto_mwhqte.jpg",
            "title": "Pechugas de pollo al Oporto",
            "description": "Cortamos las pechugas de pollo en dos trozos y las pasamos por la sartén hasta que se doren ligeramente por fuera y las reservamos. En el aceite que ha quedado en la sartén sofreímos la cebolla cortada en brunoise y, cuando empiece a tomar color añadimos los champiñones troceados, damos unas vueltas y añadimos el pollo que tenemos reservado. Echamos la salsa de soja y el vino de Oporto, subimos el fuego para que se evapore el alcohol. Cuando deje de oler a alcohol, añadimos la nata, bajamos el fuego y dejamos a fuego lento durante unos cinco minutos. Servimos las pechugas de pollo calientes acompañadas de unas patatas fritas que podemos ir preparando en otra sartén mientras se hace el pollo.",
            "private": False,
            "tag": 3,
            "id_user": 100000001,
        },
        {
            "id": 10003,
            "photo": "https://res.cloudinary.com/dw4npwftd/image/upload/v1647882901/Alubias_con_verduras_enrxus.png",
            "title": "Alubias con verduras",
            "description": "La noche anterior, poner a remojo las alubias en abundante agua con sal. Dejar remojando, al menos, 12 horas. Colar las alubias y poner, con agua nueva, en una olla. Poner dentro también las zanahorias, las hebras de azafrán, los puerros y los tomates secos. Añadir un poco de sal. Comenzar a hervir a fuego fuerte y, cuando rompa a hervir, bajar el fuego al mínimo y tapar con una tapa de manera que salga una rendija de vapor. Cocer durante unos 50 minutos o hasta que las alubias estén bien tiernas. Cuando las alubias estén tiernas, poner en un vaso batidor el tomate seco, la zanahoria y los puerros con un poco del caldo de la cocción y triturar bien. Añadir el puré a las fabes y mezclar con el vaivén de la olla simplemente. Poner a punto de sal las alubias. Pelar la calabaza, quitar las pepitas y las hebras interiores y cortar en cubitos. Saltear en una sartén con el aceite de oliva y las hierbas y un poco de sal a fuego alegre. Cuando empiece a tomar color, añadir las setas limpias y también troceadas y terminar de saltear durante un par de minutos. Agregar las verduras salteadas por encima de las fabes y terminar con un chorrito de aceite de oliva en crudo por encima.",
            "private": False,
            "tag": 1,
            "id_user": 100000001,
        },
        # {
        #     "id": 10004,
        #     "photo": "",
        #     "title": "",
        #     "description": "",
        #     "private": False,
        #     "tag": 0,
        #     "id_user": 100000001,
        # },
    ],
    "Menu":[
        {
            "id": 1000,
            "title": "Menus ligth",
            "create_at": datetime.datetime.now(),
            "id_user": 100000002,
        },
        {
            "id": 1002,
            "title": "Menus niños",
            "create_at":  datetime.datetime.now(),
            "id_user": 100000002,
        },
        {
            "id": 1003,
            "title": "Menu verano",
            "create_at": datetime.datetime.now(),
            "id_user": 100000001,
        }

    ],
    "Recipe_menu":[
        {
            "id": 1000001,
            "id_menu":1002,
            "id_recipe": 10000,
        },
        {
            "id": 1000002,
            "id_menu": 1002,
            "id_recipe": 10001,
        },
        {
            "id": 1000003,
            "id_menu": 1002,
            "id_recipe": 10002,
        },
    ],
    "RecipeIngredient":[
        {
            "id": 100000,
            "id_ingredient": 131,
            "id_recipe": 10000,
        },
        {
            "id": 100001,
            "id_ingredient": 139,
            "id_recipe":  10000,
        },
        {
            "id": 100002,
            "id_ingredient": 129,
            "id_recipe":  10000,
        },
        {
            "id": 100003, 
            "id_ingredient": 244,
            "id_recipe": 10000, 
        },
        {
            "id": 100004, 
            "id_ingredient": 209,
            "id_recipe": 10000, 
        },
        {
            "id": 100005, 
            "id_ingredient": 110,
            "id_recipe": 10000, 
        },
        {
            "id": 100006, 
            "id_ingredient": 217,
            "id_recipe": 10000, 
        },
        {
            "id": 100007, 
            "id_ingredient": 248,
            "id_recipe": 10001, 
        },
        {
            "id": 100008, 
            "id_ingredient": 253,
            "id_recipe": 10001, 
        },
        {
            "id": 100009, 
            "id_ingredient": 245,
            "id_recipe": 10001, 
        },
        {
            "id": 100010, 
            "id_ingredient": 254,
            "id_recipe": 10001, 
        },
        {
            "id": 100011, 
            "id_ingredient": 251,
            "id_recipe": 10001, 
        },
        {
            "id": 100012, 
            "id_ingredient": 252,
            "id_recipe": 10001, 
        },
        {
            "id": 100013, 
            "id_ingredient": 255,
            "id_recipe": 10001, 
        },
        {
            "id": 100014, 
            "id_ingredient": 110,
            "id_recipe": 10001, 
        },
        {
            "id": 100015, 
            "id_ingredient": 209,
            "id_recipe": 10001, 
        },
        {
            "id": 100016, 
            "id_ingredient": 150,
            "id_recipe": 10002, 
        },
        {
            "id": 100017, 
            "id_ingredient": 256,
            "id_recipe": 10002, 
        },
        {
            "id": 100018, 
            "id_ingredient": 126,
            "id_recipe": 10002, 
        },
        {
            "id": 100019, 
            "id_ingredient": 257,
            "id_recipe": 10002, 
        },
        {
            "id": 100020, 
            "id_ingredient": 129,
            "id_recipe": 10002, 
        },
        {
            "id": 100021, 
            "id_ingredient": 258,
            "id_recipe": 10002, 
        },
        {
            "id": 100022, 
            "id_ingredient": 223,
            "id_recipe": 10002, 
        },
        {
            "id": 100023, 
            "id_ingredient": 230,
            "id_recipe": 10003, 
        },
        {
            "id": 100024, 
            "id_ingredient": 259,
            "id_recipe": 10003, 
        },
        {
            "id": 100025, 
            "id_ingredient": 139,
            "id_recipe": 10003, 
        },
        {
            "id": 100026, 
            "id_ingredient": 260,
            "id_recipe": 10003, 
        },
        {
            "id": 100027, 
            "id_ingredient": 255,
            "id_recipe": 10003, 
        },
        {
            "id": 100028, 
            "id_ingredient": 209,
            "id_recipe": 10003, 
        },
        {
            "id": 100029, 
            "id_ingredient": 131,
            "id_recipe": 10003, 
        },
        {
            "id": 100030, 
            "id_ingredient": 216,
            "id_recipe": 10003, 
        },
        {
            "id": 100031, 
            "id_ingredient": 207,
            "id_recipe": 10003, 
        },
        {
            "id": 100032, 
            "id_ingredient": 217,
            "id_recipe": 10003, 
        },
        {
            "id": 100033, 
            "id_ingredient": 140,
            "id_recipe": 10003, 
        },
    ]
}