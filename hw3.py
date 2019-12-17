#--------------------- Askisi 1 -----------------------

def location(name, lat, lon, type):
    """Kataskeuazei syn8eto dedomeno topo8esias (location).

    name -- onoma (str)
    lat -- gewfrafiko platos (se moires)
    lon -- gewgrafiko mikos (se moires)
    type -- eidos topo8esias (str)

    Epistrefei dedomeno pou anaparista tin topo8esia me onoma name h opoia
    brisketai sto gewgrafiko platos kai mikos lat kai lon antistoixa. To type
    einai string pou perigrafei to eidos tis topo8esias, p.x., 'monument',
    'bus station'.
    """
    return [name, lat,lon,type]


def name(loc):
    """Epistrefei to onoma mias topo8esias.

    loc -- topo8esia (typou location)

    Epistrefei to onoma (str) tis topo8esias loc.

    >>> monast = location('Monastiraki', 37.976362, 23.725947, 'square')
    >>> name(monast)
    'Monastiraki'
    """
    return loc[0]

def longitude(loc):
    """Gewgrafiko mikos.

    loc -- dedomeno location

    Epistrefei gewgrafiko mikos tis topo8esias loc

    >>> monast = location('Monastiraki', 37.976362, 23.725947, 'square')
    >>> longitude(monast)
    23.725947
    """
    return loc[2]

def lattitude(loc):
    """Gewgrafiko platos.

    loc -- dedomeno location

    Epistrefei gewgrafiko mikos tis topo8esias loc

    >>> monast = location('Monastiraki', 37.976362, 23.725947, 'square')
    >>> lattitude(monast)
    37.976362
    """
    return loc[1]


def type(loc):
    """Eidos topo8esias.

    loc -- dedomeno location

    Epistrefei string pou perigrafei to eidos tis topo8esias loc, p.x.,
    'monument', 'bus station'.

    >>> monast = location('Monastiraki', 37.976362, 23.725947, 'square')
    >>> type(monast)
    'square'
    """
    return loc[3]



#--------------------- Askisi 2 -----------------------

def distance(a, b):
    """Apostasi meta3y topo88esiwn.

    a -- topo8esia A (dedomeno typou location)
    b -- topo8esia B (dedomeno typou location)

    Epistrefei tin apostasi (Manhattan distance) 
    meta3y ths topo8esias A kai B se xiliometra.

    >>> aueb = location('AUEB', 37.994097, 23.732253, 'university campus')
    >>> monast = location('Monastiraki', 37.976362, 23.725947, 'square')
    >>> distance(aueb, monast)
    2.5224714882938657
    >>> distance(aueb, aueb)
    0.0
    """
    """ALLA3TE TON KWDIKA."""
    
    lat_dist = (longitude(a) - longitude(b)) 
    lon_dist = (lattitude(a) - lattitude(b))
    return abs(lon_dist) + abs(lat_dist)


def print_location(loc):
    """Emfanizei stoixeia topo8esias.

    loc -- dedomeno location

    Emfanizei stoixeia gia tin topo8esia loc opws sta paradeigmata:

    >>> monast = location('Monastiraki', 37.976362, 23.725947, 'square')
    >>> print_location(monast)
    Monastiraki (square) at coordinates 37.976362, 23.725947
    >>> print_location(location('North Pole', 90.0, 135.0, 'pole'))
    North Pole (pole) at coordinates 90.0, 135.0
    """
    """GRAPSTE TON KWDIKA SAS APO KATW."""


def nearest_location(loc, loc_list, loc_type=None):
    """Epistrefei plisiesteri topo8esia.

    loc -- topo8esia (dedomeno typoy location)
    loc_list -- lista pou periexei topo8esies (dedomena location)
    loc_type -- eidos topo8esias (str)

    Epistrefei tin plisiesteri topo8esia stin loc apo autes pou briskonai sti
    lista loc_list tou eidous loc_type.

    Paradeigmata:
    >>> llist = [location('AUEB', 37.994097, 23.732253, 'university campus'),\
                  location('Acropolis', 37.971584, 23.725912, 'monument'), \
                  location('Syntagma', 37.975560, 23.734691, 'square'), \
                  location('National Garden', 37.973116, 23.736483, 'park'), \
                  location('Monastiraki', 37.976362, 23.725947, 'square')]
    >>> name(nearest_location(llist[2], llist, 'monument'))
    'Acropolis'
    >>> name(nearest_location(llist[1], llist, 'square'))
    'Monastiraki'
    >>> name(nearest_location(llist[2], llist))
    'National Garden'
    >>> name(nearest_location(llist[2], llist, 'square'))
    'Monastiraki'
    """
    """GRAPSTE TON KWDIKA SAS APO KATW."""
    
    if loc_type is None:
        locs_with_type = loc_list
    else:
        locs_with_type = [location for location in loc_list if location[3] == loc_type]

    #create list of tuple(distance,loc_name)
    locs = [[distance(loc,location),location[0]] for location in locs_with_type] 
    #find min distance
    _min = min(locs,key = lambda k:k[0])
    for location in locs:
        if location[0] is _min:
            return location[1]
    
    return 'error' 





#--------------------- Askisi 3 -----------------------

def pick_cherries_only():
    """Emfanizei string pou briskontai se fwliasmenes listes.

    Prepei na exei to akolou8o apotelesma:

    >>> pick_cherries_only()
    cherry1
    cherry2
    cherry3
    cherry4
    Yay!!!
    """
    """ SYMPLHRWSTE TA KENA APO KATW."""
    fruits = ['cherry1', 'orange', \
              ['grape', 'cherry2', ['cherry3'], 'banana'], \
              None, 'cherry4', [[['Yay!!!']]]]

    print(fruits[0])
    print(fruits__________________)
    print(fruits__________________)
    print(fruits__________________)
    print(fruits__________________)
        

#--------------------- Askisi 4 -----------------------

def pick_cherries_onebyone():
    """Emfanizei string pou briskontai se fwliasmenes listes.

    Prepei na exei to akolou8o apotelesma:

    >>> pick_cherries_onebyone()
    cherry1
    cherry2
    cherry3
    cherry4
    last cherry
    """
    """ SYMPLHRWSTE TA KENA APO KATW."""
    cherry_field = ['cherry1', ['cherry2', ['cherry3', ['cherry4', ['last cherry', None]]]]]

    print(cherry_field[0])
    cherry_field = cherry_field[1]
    print(cherry_field[0])
    cherry_field = cherry_field[1]
    print(cherry_field[0])
    cherry_field = cherry_field[1]
    print(cherry_field[0])
    cherry_field = cherry_field[1]
    print(cherry_field[0])


#--------------------- Askisi 5 -----------------------

def pick_cherries(field):
    """Emfanizei string pou briskontai se fwliasmenes listes.

    field -- lista me fwliasmena string. Ka8e lista exei dyo stoixeia: 
    to prwto einai string kai to deutero einai eite lista ths idias 
    morfhs 'h None. (Opws kai h cherry_field sto swma ths synarthshs 
    pick_cherries_onebyone()).

    Leitoyrgei opws i pick_cherries_onebyone, omws gia au8aireta polles
    fwliasmenes listes stin field.

    Paradeigmata:

    >>> cherry_field = ['cherry1', ['cherry2', ['cherry3', ['cherry4', ['last cherry', None]]]]]
    >>> pick_cherries(cherry_field)
    cherry1
    cherry2
    cherry3
    cherry4
    last cherry
    >>> pick_cherries(['Hello', ['world', None]])
    Hello
    world
    """
    """ SYMPLHRWSTE TA KENA APO KATW."""
    #s = field[0]
    l = field
    while l != None :
        s = l[0]
        print(s)
        l = l[1]


#--------------------- Askisi 6 -----------------------

def flatten(field):
    """Epistrefei lista afairwntas fwliasmenes listes.

    field -- lista me fwliasmena string. Ka8e lista exei dyo stoixeia: 
    to prwto einai string kai to deutero einai eite lista ths idias 
    morfhs 'h None. (Opws kai h cherry_field sto swma ths synarthshs 
    pick_cherries_onebyone()).

    Epistrefei nea lista pou periexei ola ta string pou briskontai sti
    field, xwris omws na periexontai se fwliasmenes listes.

    Paradeigmata:

    >>> cherry_field = ['cherry1', ['cherry2', ['cherry3', ['cherry4', ['last cherry', None]]]]]
    >>> flatten(cherry_field)
    ['cherry1', 'cherry2', 'cherry3', 'cherry4', 'last cherry']
    >>> flatten(['Hello', ['world', None]])
    ['Hello', 'world']
    >>> flatten(['Lone cherry', None])
    ['Lone cherry']
    """
    """GRAPSTE TON KWDIKA SAS APO KATW."""
    l = field 
    res = []
    while l != None:
        res.append(l[0])
        l = l[1]
    print(res)



#--------------------- Askisi 7 -----------------------

def cherry_string(field):
    """String me ola ta string pou periexoun 'cherry' sti field.

    field -- lista me fwliasmena string. Ka8e lista exei dyo stoixeia: 
    to prwto einai string kai to deutero einai eite lista ths idias 
    morfhs 'h None. 
    (Opws kai h cherry_field sto swma ths synarthshs pick_cherries_onebyone()).

    Epistrefei string pou exei proel8ei apo synenwsh olwn twn string
    pou periexontai sti field kai periexoun th le3h 'cherry'.

    Paradeigmata:

    >>> cherry_field = ['cherry1', ['cherry2', ['cherry3', ['cherry4', ['last cherry', None]]]]]
    >>> cherry_string(cherry_field)
    'cherry1cherry2cherry3cherry4last cherry'
    >>> cherry_string(['Hello', ['cherry', None]])
    'cherry'
    >>> cherry_string(['Hello', ['first cherry', ['world', ['last cherry', None]]]])
    'first cherrylast cherry'
    """
    """ SYMPLHRWSTE TA KENA APO KATW."""

    #maybe instructor doesn't want this-we should implement a one liner for this
    from functools import reduce
    from operator import concat
    def filter_cherry(s):
        if 'cherry' in s:
            return True
        else:
            return False

    def strs_from_fields(field):
        l = field 
        res = []
        while l != None:
            res.append(l[0])
            l = l[1]
        return res

    return reduce(concat,filter(filter_cherry,strs_from_fields(field)))


#--------------------- Askisi 8 -----------------------

def unflatten(ls):
    """Epistrefei stoixeia topo8etwntas ta se fwliasmenes listes.

    ls -- lista pou ta stoixeia tis einai string.

    Epistrefei lista me fwliasmena string, opws to orisma ths synarthshs 
    cherry string. Mia tetoia lista exei dyo stoixeia: to prwto einai
    string kai to deutero einai eite lista ths idias morfhs 'h None.

    Paradeigmata:

    >>> unflatten(['Hello', 'world'])
    ['Hello', ['world', None]]
    >>> unflatten(['Hello'])
    ['Hello', None]
    >>> unflatten(['No', 'more', 'cherries', 'please!'])
    ['No', ['more', ['cherries', ['please!', None]]]]
    """
    """GRAPSTE TON KWDIKA SAS APO KATW."""
    l = None
    ls.reverse()
    for s in ls:
        l = [s,l]
    return l     

