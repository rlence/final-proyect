from api.shared.encrypte_pass import encryp_pass
import datetime
from datetime import timedelta


data = {
    
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
}