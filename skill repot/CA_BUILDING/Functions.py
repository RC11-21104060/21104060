import csv, random

def write(currentState, counter):
    with open('state000000' + str(counter) + '.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for row in currentState:
            r = []
            for c in row:
                if c.type == 'solornons seal':
                    r.append(1)
                elif c.type == 'lamier jaune':
                    r.append(2)
                elif c.type == 'sessile oak':
                    r.append(3)
                elif c.type == ' Algerian Iris':
                    r.append(4)
                elif c.type == 'lierre gri':
                    r.append(5)
                elif c.type == 'sureau rou':
                    r.append(6)
                elif c.type == 'Nerprun al':
                    r.append(7)
                elif c.type == 'Prunelier':
                    r.append(8)
                elif c.type == 'Tamaris de France':
                    r.append(9)
                elif c.type == 'Tamaris Afrique':
                    r.append(10)
                elif c.type == 'Sureau noir':
                    r.append(11)
                elif c.type == 'Sumac de Virginie':
                    r.append(12)
                elif c.type == 'Large-leaved':
                    r.append(13)
                elif c.type == 'European ash':
                    r.append(14)
                elif c.type == 'Sycamore maple':
                    r.append(15)
                elif c.type == 'Beech':
                    r.append(16)
                elif c.type == 'Sessile oak':
                    r.append(17)
                elif c.type == 'Pedunculate oak':
                    r.append(18)
                elif c.type == 'Red oak':
                    r.append(19)
                else:
                    r.append(0)
            spamwriter.writerow(r)

def read(filename, currentState):
    with open(filename) as csvfile:
        spamreader = csv.reader(csvfile)
        rownr = 0
        for row in spamreader:
            colnr = 0
            for v in row:
                cell = currentState[rownr][colnr]
                if v == '0':
                    cell.changeType('dead')
                if v == '1':
                    cell.changeType('solornons seal')
                if v == '2':
                    cell.changeType('lamier jaune')
                if v =='3':
                    cell.changeType('Algerian Iris')
                if v =="4":
                    cell.changeType('solidago vir')
                if v =="5":
                    cell.changeType('lierre gri')
                if v =="6":
                    cell.changeType('sureau rou')
                if v =="7":
                    cell.changeType('Nerprun al')
                if v =="8":
                    cell.changeType('Prunelier')
                if v =="9":
                    cell.changeType('Tamaris de France')
                if v =="10":
                    cell.changeType('Tamaris Afrique')
                if v =="11":
                    cell.changeType('Sureau noir')
                if v =="12":
                    cell.changeType('Sumac de Virginie')
                if v =="13":
                    cell.changeType('Large-leaved')
                if v =="14":
                    cell.changeType('European ash')
                if v =="15":
                    cell.changeType('Sycamore maple')
                if v =="16":
                    cell.changeType('Beech')
                if v =="17":
                    cell.changeType('Sessile oak')
                if v =="18":
                    cell.changeType('Pedunculate oak')
                if v =="19":
                    cell.changeType('Red oak')
                # keep going for all values corresponding to tree types
                colnr += 1
            rownr += 1

#def read_Fertility(filename, currentState):
    #with open(filename) as csvfile:
       #spamreader = csv.reader(csvfile)
        #rownr = 0
        #for row in spamreader:
            #colnr = 0
            #for v in row:
                #cell = currentState[rownr][colnr]
                #cell.fertility = int(v)

                #colnr += 1
            #rownr += 1

def get_neighbours(location, currentState):
    lx = location[0]
    ly = location[1]

    # solornonsseal = 0
    # lamierjaune = 0
    # AlgerianIris = 0
    # solidagovir = 0
    # lierregri = 0
    # sureaurou = 0
    # Nerprunal = 0
    # Pruneliers = 100
    # TamarisdeFrance = 0
    # TamarisAfrique = 0
    # Sureaunoir = 0
    # SumacdeVirginie = 0
    # Largeleaved = 0
    # Europeanash = 0
    # Sycamoremaple = 0
    # Beechs = 0
    # Sessileoak = 0
    # Pedunculateoak = 0
    # Redoak = 0
    # dead = 0

    solornonsseal = 1000
    lamierjaune = 1000
    AlgerianIris = 1000
    solidagovir = 1000
    lierregri = 1000
    sureaurou = 1000
    Nerprunal = 1000
    Pruneliers =1000
    TamarisdeFrance = 1000
    TamarisAfrique = 1000
    Sureaunoir = 1000
    SumacdeVirginie = 1000
    Largeleaved = 1000
    Europeanash = 1000
    Sycamoremaple = 1000
    Beechs = 1000
    Sessileoak = 1000
    Pedunculateoak = 1000
    Redoak = 1000
    dead = 1000

    for i in range(-1, 2):
        for j in range(-1,2):
            if not i==j==0:
                if not (lx+i < 0 or ly+j < 0 or lx+i >= len(currentState) or ly+j >= len(currentState[0])):
                    neighbour = currentState[lx+i][ly+j].type
                    if neighbour == 'solornons seal':
                        solornonsseal += 1
                    elif neighbour == 'lamier jaune':
                        lamierjaune += 1
                    elif neighbour == 'Algerian Iris':
                         AlgerianIris += 1
                    elif neighbour == 'solidago vir':
                        solidagovir += 1
                    elif neighbour == 'lierre gri':
                        lierregri += 1
                    elif neighbour == 'sureau rou':
                        sureaurou += 1
                    elif neighbour == 'Nerprun al':
                        Nerprunal += 1
                    elif neighbour == 'Prunelier':
                        Pruneliers += 1
                    elif neighbour == 'Tamaris de France':
                        TamarisdeFrance += 1
                    elif neighbour == 'Tamaris Afrique':
                        TamarisAfrique += 1
                    elif neighbour == 'Sureau noir':
                        Sureaunoir += 1
                    elif neighbour == 'Sumac de Virginie':
                        SumacdeVirginie += 1
                    elif neighbour == 'Large-leaved':
                        Largeleaved += 1
                    elif neighbour == 'European ash':
                        Europeanash += 1
                    elif neighbour == 'Sycamore maple':
                        Sycamoremaple += 1
                    elif neighbour == 'Beech':
                        Beechs += 1
                    elif neighbour == 'Sessile oak':
                        Sessileoak += 1
                    elif neighbour == 'Pedunculate oak':
                        Pedunculateoak += 1
                    elif neighbour == 'Red oak':
                        Redoak += 1

    return [solornonsseal,lamierjaune,AlgerianIris,solidagovir,lierregri ,sureaurou,Nerprunal,Pruneliers,TamarisdeFrance,TamarisAfrique ,Sureaunoir,SumacdeVirginie,Largeleaved,Europeanash,Sycamoremaple,Beechs,Sessileoak,Pedunculateoak,Redoak,dead
]

def get_next_state(location, currentState):
    lx = location[0]
    ly = location[1]
    current_type = currentState[lx][ly].type
    # Maybe rename this to neighbouring_Plants, as it isn't live or dead anymore
    live_neighbours = get_neighbours(location, currentState)

    ## You don't need both, since these function return the exact same (the array on line 185)
    dead_neighbours = get_neighbours(location, currentState)

    # these will now always stay 0, you didn't assign a value to them.
    # maybe instead of using an array, try unsing a dictionary, this will make it much easier for You
    # to keep track of all the different names.


    solornonsseal = 1000
    lamierjaune = 1000
    AlgerianIris = 1000
    solidagovir = 1000
    lierregri = 1000
    sureaurou = 1000
    Nerprunal = 1000
    Pruneliers =1000
    TamarisdeFrance = 1000
    TamarisAfrique = 1000
    Sureaunoir = 1000
    SumacdeVirginie = 1000
    Largeleaved = 1000
    Europeanash = 1000
    Sycamoremaple = 1000
    Beechs = 1000
    Sessileoak = 1000
    Pedunculateoak = 1000
    Redoak = 1000
    dead = 1000

    #fertility = currentState[lx][ly].fertility

    # # Things like live_neighbours==2 doesn't mean anything anymore since live_neighbours is now an array
    # if current_type == 'dead' and solornonsseal >= 2:
    # #     #r = random.randint(0,3)
    # #     #if r < fertility:
    # #         #return 'solornons seal'
    # #     #else:
    #         return solornonsseal
    # elif current_type == 'solornons seal' and dead_neighbours == 2:
    #     return dead
    # elif current_type == 'Lamier jaune' and solornonsseal >= 2:
    #     return solornonsseal
    # elif current_type == 'Lamier jaune' and (solornonsseal == 1):
    #     return AlgerianIris
    #
    # elif current_type == 'Algerian Iris' and lamierjaune >= 2:
    #     return lamierjaune
    # elif current_type == 'Algerian Iris' and (lamierjaune == 1):
    #     return solidagovir
    #
    # elif current_type == 'solidago vir' and AlgerianIris >= 2:
    #     return AlgerianIris
    # elif current_type == 'solidago vir' and (AlgerianIris== 1):
    #     return lierregri
    #
    # elif current_type == 'lierre gri' and solidagovir >= 2:
    #     return solidagovir
    # elif current_type == 'lierre gri' and (solidagovir== 1):
    #     return sureaurou
    #
    # elif current_type == 'sureau rou' and lierregri >= 2:
    #     return lierregri
    # elif current_type == 'sureau rou' and (lierregri== 1):
    #     return Nerprunal
    #
    # elif current_type == 'Nerprun al' and sureaurou >= 2:
    #     return sureaurou
    # elif current_type == 'Nerprun al' and (sureaurou== 1):
    #     return Pruneliers
    #
    # elif current_type == 'Prunelier' and Nerprunal >= 2:
    #     return Nerprunal
    # elif current_type == 'Prunelier' and (Nerprunal== 1):
    #     return TamarisdeFrance
    #
    # elif current_type == 'Tamaris de France' and Pruneliers >= 2:
    #     return Pruneliers
    # elif current_type == 'Tamaris de France' and (Pruneliers== 1):
    #     return TamarisAfrique
    #
    # elif current_type == 'Tamaris Afrique' and TamarisdeFrance >= 2:
    #     return TamarisdeFrance
    # elif current_type == 'Tamaris Afrique' and (TamarisdeFrance== 1):
    #     return Sureaunoir
    #
    # elif current_type == 'Sureau noir' and TamarisAfrique  >= 2:
    #     return TamarisdeFrance
    # elif current_type == 'Sureau noir' and (TamarisAfrique == 1):
    #     return SumacdeVirginie
    #
    # elif current_type == 'Sumac de Virginie' and Sureaunoir >= 2:
    #     return TamarisdeFrance
    # elif current_type == 'Sumac de Virginie' and (Sureaunoir== 1):
    #     return Largeleaved
    #
    # elif current_type == 'Large-leaved' and SumacdeVirginie >= 2:
    #     return SumacdeVirginie
    # elif current_type == 'Large-leaved' and (SumacdeVirginie== 1):
    #     return Europeanash
    #
    # elif current_type == 'European ash' and Largeleaved  >= 2:
    #     return Largeleaved
    # elif current_type == 'European ash' and (Largeleaved == 1):
    #     return Sycamoremaple
    #
    # elif current_type == 'Sycamore maple' and Europeanash >= 2:
    #     return Europeanash
    # elif current_type == 'Sumac de Virginie' and (Europeanash== 1):
    #     return Beechs
    #
    # elif current_type == 'Beech' and Sycamoremaple >= 2:
    #     return Sycamoremaple
    # elif current_type == 'Beech' and (Sycamoremaple== 1):
    #     return Sessileoak
    #
    # elif current_type == 'Sessile oak' and Beechs >= 2:
    #     return Beechs
    # elif current_type == 'Sessile oak' and (Beechs== 1):
    #     return Pedunculateoak
    #
    # elif current_type == 'Pedunculate oak' and Sessileoak >= 2:
    #     return Sycamoremaple
    # elif current_type == 'Pedunculate oak' and (Sessileoak== 1):
    #     return Redoak
    #
    # elif current_type == 'Red oak' and Pedunculateoak >= 2:
    #     return Pedunculateoak
    #
    # else:
    #     return 'current_type'
    # #fertility = currentState[lx][ly].fertility

    # Things like live_neighbours==2 doesn't mean anything anymore since live_neighbours is now an array
    if current_type == 'dead' and solornonsseal >= 2:
        #r = random.randint(0,3)
        #if r < fertility:
            #return 'solornons seal'
        #else:
            return solornonsseal
    elif current_type == 'solornons seal' and dead_neighbours == 2:
        return dead
    elif current_type == 'Lamier jaune' and (solornonsseal >= 2 or AlgerianIris>= 2 or solidagovir >=2 or lierregri >=2 or dead >= 2):
        return solornonsseal
    elif current_type == 'Lamier jaune' and (solornonsseal == 1 or AlgerianIris == 1 or solidagovir == 1 or lierregri ==1):
        return AlgerianIris

    elif current_type == 'Algerian Iris' and (lamierjaune >= 2 or solornonsseal >= 2 or solidagovir >= 2 or lierregri >=2 or dead >= 2):
        return lamierjaune
    elif current_type == 'Algerian Iris' and (lamierjaune == 1 or solornonsseal == 1 or solidagovir == 1 or lierregri ==1):
        return solidagovir

    elif current_type == 'solidago vir' and (AlgerianIris >= 2 or lamierjaune >= 2 or solornonsseal >= 2 or lierregri >=2 or dead >= 2):
        return AlgerianIris
    elif current_type == 'solidago vir' and (AlgerianIris== 1 or lamierjaune == 1 or solornonsseal == 1 or lierregri ==1):
        return lierregri

    elif current_type == 'lierre gri' and (solidagovir >= 2 or AlgerianIris >= 2 or lamierjaune >= 2 or solornonsseal >= 2 or dead >= 2):
        return solidagovir
    elif current_type == 'lierre gri' and (solidagovir== 1 or AlgerianIris == 1 or lamierjaune == 1 or solornonsseal == 1):
        return sureaurou

    elif current_type == 'sureau rou' and (lierregri >= 2 or Nerprunal >= 2 or Pruneliers >= 2 or TamarisdeFrance >= 2 or TamarisAfrique >= 2 or Sureaunoir >= 2 or SumacdeVirginie >= 2 or dead >= 2):
        return lierregri
    elif current_type == 'sureau rou' and (lierregri== 1 or Nerprunal == 1 or Pruneliers == 1 or TamarisdeFrance == 1 or TamarisAfrique ==1 or Sureaunoir == 1 or SumacdeVirginie == 1 ):
        return Nerprunal

    elif current_type == 'Nerprun al' and (sureaurou >= 2 or lierregri >= 2 or Pruneliers >= 2 or TamarisdeFrance >= 2 or TamarisAfrique >= 2 or Sureaunoir >= 2 or SumacdeVirginie >= 2 or dead >= 2):
        return sureaurou
    elif current_type == 'Nerprun al' and (sureaurou== 1 or lierregri == 1 or Pruneliers == 1 or TamarisdeFrance == 1 or TamarisAfrique == 1 or Sureaunoir == 1 or SumacdeVirginie == 1):
        return Pruneliers

    elif current_type == 'Prunelier' and (Nerprunal >= 2 or lierregri >= 2 or Nerprunal >= 2 or TamarisdeFrance >= 2 or TamarisAfrique >= 2 or Sureaunoir >= 2 or SumacdeVirginie >= 2 or dead >= 2):
        return Nerprunal
    elif current_type == 'Prunelier' and (Nerprunal== 1 or lierregri == 1 or Nerprunal == 1 or TamarisdeFrance == 1 or TamarisAfrique == 1 or Sureaunoir == 1 or SumacdeVirginie ==1 ):
        return TamarisdeFrance

    elif current_type == 'Tamaris de France' and (Pruneliers >= 2 or lierregri >= 2 or Nerprunal >= 2 or Pruneliers >= 2 or TamarisAfrique >= 2 or Sureaunoir >= 2 or SumacdeVirginie >= 2 or dead >= 2):
        return Pruneliers
    elif current_type == 'Tamaris de France' and (Pruneliers== 1 or lierregri == 1  or Nerprunal == 1 or Pruneliers == 1  or TamarisAfrique == 1 or Sureaunoir == 1 or SumacdeVirginie == 1):
        return TamarisAfrique

    elif current_type == 'Tamaris Afrique' and (TamarisdeFrance >= 2 or lierregri >= 2 or Nerprunal >= 2 or Pruneliers >= 2 or TamarisdeFrance >= 2 or Sureaunoir >= 2 or SumacdeVirginie >= 2 or dead >= 2):
        return TamarisdeFrance
    elif current_type == 'Tamaris Afrique' and (TamarisdeFrance== 1 or lierregri ==1 or Nerprunal ==1 or Pruneliers ==1 or TamarisdeFrance ==1 or Sureaunoir ==1 or SumacdeVirginie ==1 ):
        return Sureaunoir

    elif current_type == 'Sureau noir' and (TamarisAfrique  >= 2 or lierregri >= 2 or Nerprunal >= 2 or Pruneliers >= 2 or TamarisdeFrance >= 2 or TamarisAfrique >= 2 or SumacdeVirginie >= 2 or dead >= 2):
        return TamarisdeFrance
    elif current_type == 'Sureau noir' and (TamarisAfrique == 1 or lierregri ==1 or Nerprunal ==1 or Pruneliers ==1 or TamarisdeFrance ==1 or TamarisAfrique ==1 or SumacdeVirginie ==1):
        return SumacdeVirginie

    elif current_type == 'Sumac de Virginie' and (Sureaunoir >= 2 or TamarisAfrique  >= 2 or lierregri >= 2 or Nerprunal >= 2 or Pruneliers >= 2 or TamarisdeFrance >= 2 or TamarisAfrique >= 2 or dead >= 2 ):
        return TamarisdeFrance
    elif current_type == 'Sumac de Virginie' and (Sureaunoir== 1 or TamarisAfrique  ==1 or lierregri ==1 or Nerprunal ==1 or Pruneliers ==1 or TamarisdeFrance ==1 or TamarisAfrique ==1):
        return Largeleaved

    elif current_type == 'Large-leaved' and (SumacdeVirginie >= 2 or Europeanash >= 2 or Sycamoremaple >= 2 or Beechs >= 2 or Sessileoak >= 2 or Pedunculateoak >= 2 or Redoak >= 2 or dead >= 2 ):
        return SumacdeVirginie
    elif current_type == 'Large-leaved' and (SumacdeVirginie== 1 or Europeanash ==1 or Sycamoremaple ==1 or Beechs ==1 or Sessileoak ==1 or Pedunculateoak ==1 or Redoak ==1):
        return Europeanash

    elif current_type == 'European ash' and (Largeleaved  >= 2 or SumacdeVirginie >= 2 or Sycamoremaple >= 2 or Beechs >= 2 or Sessileoak >= 2 or Pedunculateoak >= 2 or Redoak >= 2 or dead >= 2 ):
        return Largeleaved
    elif current_type == 'European ash' and (Largeleaved == 1 or SumacdeVirginie ==1 or Sycamoremaple ==1 or Beechs ==1 or Sessileoak ==1 or Pedunculateoak ==1 or Redoak ==1 ):
        return Sycamoremaple

    elif current_type == 'Sycamore maple' and (Europeanash >= 2 or SumacdeVirginie >= 2 or Beechs >= 2 or Sessileoak >= 2 or Pedunculateoak >= 2 or Redoak >= 2 or dead >= 2 ):
        return Europeanash
    elif current_type == 'Sumac de Virginie' and (Europeanash== 1 or SumacdeVirginie ==1 or Beechs ==1 or Sessileoak ==1 or Pedunculateoak ==1 or Redoak ==1):
        return Beechs

    elif current_type == 'Beech' and (Sycamoremaple >= 2 or SumacdeVirginie >= 2 or Europeanash >= 2 or Sessileoak >= 2 or Pedunculateoak >= 2 or Redoak >= 2 or dead >= 2 ):
        return Sycamoremaple
    elif current_type == 'Beech' and (Sycamoremaple== 1 or SumacdeVirginie ==1 or Europeanash ==1 or Sessileoak ==1 or Pedunculateoak ==1 or Redoak ==1):
        return Sessileoak

    elif current_type == 'Sessile oak' and (Beechs >= 2 or SumacdeVirginie >= 2 or Europeanash >= 2 or Sycamoremaple >= 2 or Pedunculateoak >= 2 or Redoak >= 2 or dead >= 2 ):
        return Beechs
    elif current_type == 'Sessile oak' and (Beechs== 1 or SumacdeVirginie ==1 or Europeanash ==1 or Sycamoremaple ==1 or Pedunculateoak ==1 or Redoak ==1):
        return Pedunculateoak

    elif current_type == 'Pedunculate oak' and (Sessileoak >= 2 or SumacdeVirginie >= 2 or Europeanash >= 2 or Sycamoremaple >= 2 or Beechs >= 2  or Redoak >= 2 or dead >= 2 ):
        return Sycamoremaple
    elif current_type == 'Pedunculate oak' and (Sessileoak== 1 or SumacdeVirginie ==1 or Europeanash ==1 or Sycamoremaple ==1 or Beechs==1  or Redoak==1 ):
        return Redoak

    elif current_type == 'Red oak' and Pedunculateoak >= 2:
        return Pedunculateoak

    else:
        return 'current_type'
