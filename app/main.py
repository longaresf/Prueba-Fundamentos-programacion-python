from string import Template
from app.service.posts.post import get_birds

URL = 'https://aves.ninjas.cl/api/birds'
birds:dict
cantidad:int = 6


def app():
    birds = get_birds(cantidad = cantidad)

    url_img = birds["data"][0]["images"]["thumb"]
    nom_esp = birds["data"][0]["name"]["spanish"]
    nam_eng = birds["data"][0]["name"]["english"]
    url_img1 = birds["data"][1]["images"]["thumb"]
    nom_esp1 = birds["data"][1]["name"]["spanish"]
    nam_eng1 = birds["data"][1]["name"]["english"]
    url_img2 = birds["data"][2]["images"]["thumb"]
    nom_esp2 = birds["data"][2]["name"]["spanish"]
    nam_eng2 = birds["data"][2]["name"]["english"]
    url_img3 = birds["data"][3]["images"]["thumb"]
    nom_esp3 = birds["data"][3]["name"]["spanish"]
    nam_eng3 = birds["data"][3]["name"]["english"]
    url_img4 = birds["data"][4]["images"]["thumb"]
    nom_esp4 = birds["data"][4]["name"]["spanish"]
    nam_eng4 = birds["data"][4]["name"]["english"]
    url_img5 = birds["data"][5]["images"]["thumb"]
    nom_esp5 = birds["data"][5]["name"]["spanish"]
    nam_eng5 = birds["data"][5]["name"]["english"]
    html = html_template.substitute(img_0 = url_img, eng_0 = nam_eng, nom_0 = nom_esp, img_1 = url_img1, eng_1 = nam_eng1, nom_1 = nom_esp1, img_2 = url_img2, eng_2 = nam_eng2, nom_2 = nom_esp2, img_3 = url_img3, eng_3 = nam_eng3, nom_3 = nom_esp3, img_4 = url_img4, eng_4 = nam_eng4, nom_4 = nom_esp4, img_5 = url_img5, eng_5 = nam_eng5, nom_5 = nom_esp5)

    f = open("index.html", "x")
    f.writelines({html})
    f.close()

    print(f'html: {html}')
    return {
         "statusCode": 200,
         "body": html,
        "headers": {"Content-Type": "text/html"}
        }



html_template = Template('''
                             <!DOCTYPE html>
                                <html lang="es">
                                <head>
                                    <title>AVES DE CHILE</title>
                                    <meta name="author" content="Francisco Longares">
                                    <meta charset="UTF-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
                                    <link rel="preconnect" href="https://fonts.googleapis.com">
                                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                                    <link href="https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
                                    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
                                    <link rel="stylesheet" href="assets/css/style.css">
                                    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js" integrity="sha512-v2CJ7UaYy4JwqLDIrZUI/4hqeoQieOmAZNXBeQyjo21dadnwR+8ZaIJVT8EE2iyI61OV8e6M8PP2/4hpQINQ/g==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
                                </head>
                                <body>
                                <h1 class="text-center">AVES DE CHILE</h1>
                            <div class="card-birds row row-cols-1 row-cols-md-3 g-4">
                         <div class="col"><div class="card w-80"><img src=$img_0 class="card-img-top" alt="..."><div class="card-body"><p class="card-text"><b>Nombre:</b> $nom_0</p><p class="card-text"><b>Name:</b> $eng_0</p></div></div></div>
                        <div class="col"><div class="card w-80"><img src=$img_1 class="card-img-top" alt="..."><div class="card-body"><p class="card-text"><b>Nombre:</b> $nom_1</p><p class="card-text"><b>Name:</b> $eng_1</p></div></div></div>
                         <div class="col"><div class="card w-80"><img src=$img_2 class="card-img-top" alt="..."><div class="card-body"><p class="card-text"><b>Nombre:</b> $nom_2</p><p class="card-text"><b>Name:</b> $eng_2</p></div></div></div>
                         <div class="col"><div class="card w-80"><img src=$img_3 class="card-img-top" alt="..."><div class="card-body"><p class="card-text"><b>Nombre:</b> $nom_3</p><p class="card-text"><b>Name:</b> $eng_3</p></div></div></div>
                        <div class="col"><div class="card w-80"><img src=$img_4 class="card-img-top" alt="..."><div class="card-body"><p class="card-text"><b>Nombre:</b> $nom_4</p><p class="card-text"><b>Name:</b> $eng_4</p></div></div></div>
                        <div class="col"><div class="card w-80"><img src=$img_5 class="card-img-top" alt="..."><div class="card-body"><p class="card-text"><b>Nombre:</b> $nom_5</p><p class="card-text"><b>Name:</b> $eng_5</p></div></div></div>
                                </div>
                                </body>
                                </html>
                             ''')
