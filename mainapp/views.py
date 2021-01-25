from django.shortcuts import render
import datetime
import json


# Create your views here.
# контроллер = функция
# MVC - Model Viev Controller
# Jango - MVT = Model Viev Template
# вьюха = контроллер = функция


def index(request):
    context = {
        'title': 'geekshop Store'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    content = {
        'title': 'geekShop',
        'products': [
            {'model': 'mainapp.product',
             'pk': 1,
             'fields': {'name': 'Худи черного цвета с монограммами adidas Originals',
                        'image': 'vendor/img/products/Adidas hoodie.png',
                        'description': '',
                        'short_desc': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                        'price': '6090.00',
                        'quantity': 5,
                        'category': 7}
             },
            {'model': 'mainapp.product',
             'pk': 2,
             'fields': {'name': 'Синяя куртка The North Face',
                        'image': 'vendor/img/products/Blue_jacket_The_North_Face.png',
                        'description': '',
                        'short_desc': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пухов',
                        'price': '23725.00',
                        'quantity': 3,
                        'category': 7}
             },
            {'model': 'mainapp.product',
             'pk': 3,
             'fields': {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                        'image': 'vendor/img/products/Brown_sports_oversized-top_ASOS_DESIGN.png',
                        'description': '',
                        'short_desc': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                        'price': '3390.00',
                        'quantity': 7,
                        'category': 6}
             },
            {'model': 'mainapp.product',
             'pk': 4,
             'fields': {'name': 'Черный рюкзак Nike Heritage',
                        'image': 'vendor/img/products/Black_Nike_Heritage_backpack.png',
                        'description': '',
                        'short_desc': 'Плотная ткань. Легкий материал.',
                        'price': '2340.00',
                        'quantity': 10,
                        'category': 9}
             },
            {'model': 'mainapp.product',
             'pk': 5,
             'fields': {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                        'image': 'vendor/img/products/Black_Dr_Martens_shoes.png',
                        'description': '',
                        'short_desc': 'Гладкий кожаный верх. Натуральный материал.',
                        'price': '13590.00',
                        'quantity': 4,
                        'category': 8}
             },
            {'model': 'mainapp.product',
             'pk': 6,
             'fields': {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                        'image': 'vendor/img/products/Dark_blue_wide-leg_ASOs_DESIGN_trousers.png',
                        'description': '',
                        'short_desc': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
                        'price': '2890.00', 'quantity': 6, 'category': 7}
             }
        ]

    }
    return render(request, 'mainapp/products.html', content)
