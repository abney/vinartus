
try:
    import js
    root = js.document.getElementById("root")
    print('Got root:', root)

    def write_text (*objs):
        s = ' '.join(str(x) for x in objs)
        root.appendChild(js.document.createTextNode(s))
        root.appendChild(js.document.createElement('BR'))

    write_text('Hello, world')

    import selkie
    write_text('Selkie version =', selkie.__version__, 'file =', selkie.__file__)

except Exception as e:
    print(e)
