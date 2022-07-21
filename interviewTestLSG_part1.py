#Interview test LSG PART 1
import re

# col_no = 1000
# row_no = 1000
file = 'actionFile.txt'
expPattern = re.compile(r'[0-9]{1,3}')

def create_matrix(col_no, row_no):
    '''Generating the matrix of lights'''
    x = []
    y= []
    coordTable = {}

    for i in range(0, col_no):
        x.append(i)

    for j in range(0, row_no):
        y.append(j)

    for i in x:
        for j in y:
            coordTuple = (i, j)
            coordTable[coordTuple] = 'lightOff'

    noOfLightsOn = count_lights_on(coordTable)
    print(f'Final Results: {noOfLightsOn}')

    return noOfLightsOn


def get_action_coodinates(action, coordTable):
    '''Get coordinates for every action'''

    print(action)
    coordToBeChanged = []
    valuesAction = tuple(map(int, re.findall(expPattern, action)))
    startTo = tuple(valuesAction[0:2])
    endTo = tuple(valuesAction[2:])

    for col in coordTable.keys():
        if col[0] >= startTo[0] and col[0] <= endTo[0]:
            if col[1] >= startTo[1] and col[1] <= endTo[1]:
                coordToBeChanged.append(col)

    return coordToBeChanged


def count_lights_on(coordTable):
    '''Counting the number of light on after every action'''

    f = open(file)
    for action in f.readlines():
        if 'turn on' in action:
            turnOnCoord = get_action_coodinates(action, coordTable)

            for i in turnOnCoord:
                if i in coordTable.keys():
                    coordTable[i] = 'lightOn'             
            print(f"Number of light on after 'turn on': {len(coordTable)}")
            
        elif 'turn off' in action:
            turnOffCoord = get_action_coodinates(action, coordTable)
            
            for i in turnOffCoord:
                if i in coordTable.keys():
                    coordTable[i] = 'lightOff'

            noOfLightsOn = sum(x == 'lightOn' for x in coordTable.values())
            print(f"Number of light on after 'turn off': {noOfLightsOn}")
            
        else:
            toogleCoord = get_action_coodinates(action, coordTable)

            for i in toogleCoord:
                if i in coordTable.keys() and coordTable[i] == 'lightOn':
                    coordTable[i] = 'lightOff'
                elif i in coordTable.keys() and coordTable[i] == 'lightOff':
                    coordTable[i] = 'lightOn'

            noOfLightsOn = sum(x == 'lightOn' for x in coordTable.values())
            print(f"Number of light on after 'toogle': {noOfLightsOn}")
        
    return noOfLightsOn
        

create_matrix(1000, 1000)


