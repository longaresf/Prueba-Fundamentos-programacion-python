from string import Template
from app.service.posts.post import get_birds

URL = 'https://aves.ninjas.cl/api/birds'
birds:dict
cantidad:int = 6

def app():
    birds = get_birds(cantidad = cantidad)

    mi_body = ''

    for bird in birds["data"]:
        mi_body += f'''
            <div class="col"><div class="card w-80"><img src="{bird["images"]["thumb"]}"/>
            <div class="card-body"><p class="card-text"><p class="card-text"><b>Nombre:</b> {bird["name"]["spanish"]}</p>
            <p class="card-text"><b>Name:</b> {bird["name"]["english"]}</p></div></div></div>
            '''
    html = html_template.substitute(body = mi_body)

    print(f'html: {html}')

    f = open("index2.html", "w")
    f.writelines({html})
    f.close()

html_template = Template('''
                             <!DOCTYPE html>
                                <html lang="es">
                                <head>
                                    <title>AVES DE CHILE</title>
                                    <meta name="author" content="Francisco Longares">
                                    <meta charset="UTF-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
                                    </head>
                                    <body>
                                    <h1 class="text-center">AVES DE CHILE</h1>
                                    <div class="card-birds row row-cols-1 row-cols-md-3 g-4">
                                    $body</div></body></html>
                             ''')
