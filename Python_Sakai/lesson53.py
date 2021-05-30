def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

menu(entree='beef', drink='coffee')

d = {
    'entree':'beef',
    'drink':'ice coffee',
    'dessert':'ice'
}
menu(**d)