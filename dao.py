def get_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    },
        {
            'id': 2,
            'name': 'Tablet'
        }]


def get_products(kw, slug):
    products = [{
        'id': 1,
        'name': 'Mobile',
        'price': 10000000,
        'image': 'https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg',
        'category_id': 1
    },
        {
            'id': 2,
            'name': 'Mobile',
            'price': 10000000,
            'image': 'https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg',
            'category_id': 1
        },
        {
            'id': 3,
            'name': 'Mobile',
            'price': 10000000,
            'image': 'https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg',
            'category_id': 1
        },

        {
            'id': 4,
            'name': 'Mobile',
            'price': 10000000,
            'image': 'https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg',
            'category_id': 1
        },
        {
            'id': 5,
            'name': 'Mobile',
            'price': 10000000,
            'image': 'https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg',
            'category_id': 1
        },
        {
            'id': 6,
            'name': 'Mobile',
            'price': 10000000,
            'image': 'https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg',
            'category_id': 1
        },
        {
            'id': 7,
            'name': 'Mobile',
            'price': 10000000,
            'image': 'https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg',
            'category_id': 1
        },
        {
            'id': 8,
            'name': 'Mobile',
            'price': 10000000,
            'image': 'https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg',
            'category_id': 1
        },
        {
            'id': 9,
            'name': 'Mobile',
            'price': 10000000,
            'image': 'https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg',
            'category_id': 1
        },
        {
            'id': 10,
            'name': 'Iphone',
            'price': 10000000,
            'image': 'https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg',
            'category_id': 1
        },
    ]
    if kw:
        products = [p for p in products if p['name'].lower().find(kw.lower()) >= 0]
    if slug:
        products = [p for p in products if p['id'] == kw]

    return products
