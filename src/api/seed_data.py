from api.shared.encrypte_pass import encryp_pass

data = {
    "Rol":[
        {
            "rol_name": "client"
        },
        {
            "rol_name": "work"
        }
    ],
    "User":[
        {
            "email": 'lencericardo@gmail.com',
            "password": encryp_pass("123456"),
            "username": "rlence"
        },
         {
            "email": 'lenceriegegscardo@gmail.com',
            "password":  encryp_pass("123456"),
            "username": "rlence"
        }
    ]
}