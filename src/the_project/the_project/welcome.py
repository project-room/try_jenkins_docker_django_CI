from django.http import HttpResponse


def welcome(request):
    img = '''data:image/png;base64,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
    '''

    html = '''<!DOCTYPE html><html><head><meta charset="utf-8"><title>Welcome!</title></head>
<body>
<div class="content" >
    <img src="{img}" width="40" height="40">
    <h4>Server is up and running...</h4>
</div>
<style>
    .content {
        height: 100%; 
        margin: 15% 40%;
    }
    img { float: left; }
    h4 {
        color: #333;
        font-size: 20px;
        padding-left: 80px;
    }
</style>
</body></html>
    '''

    html = html.replace('{img}', img)
    return HttpResponse(html)
