import json
import random
from colorama import Fore, Style
import matplotlib.pyplot as plt


squadre = {
    1: "Atalanta",
    2: "Bologna",
    3: "Cagliari",
    4: "Empoli",
    5: "Fiorentina",
    6: "Genoa",
    7: "Inter",
    8: "Juventus",
    9: "Lazio",
    10: "Milan",
    11: "Napoli",
    12: "Roma",
    13: "Salernitana",
    14: "Sampdoria",
    15: "Sassuolo",
    16: "Spezia",
    17: "Torino",
    18: "Udinese",
    19: "Venezia",
    20: "Verona"
}


def printGiornata(g, i):
    print("GIORNATA ", i)

    for scontro in g:
        print(squadre[scontro[0]] + " - " + squadre[scontro[1]])


def printCalendario(c):
    print("CALENDARIO:")
    i = 1
    for giornata in c:
        printGiornata(giornata, i)
        i = i + 1
        print("\n")


def printCalendario2(c):
    print("CALENDARIO:")
    j = 1
    for g in c:
        print("GIORNATA ", j)
        for i in range(len(g) - 1):
            if i % 2 == 0:
                print(squadre[g[i]] + " - " + squadre[g[i + 1]])
        print("\n")
        j = j + 1


class Team:
    def __init__(self, force, name):
        self.force = force
        self.name = name
        self.matches = 0
        self.points = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_scored = 0
        self.goals_conceded = 0
        self.history = []

    def get_points(self):
        return self.points

    def reset(self):
        self.matches = 0
        self.points = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_scored = 0
        self.goals_conceded = 0


class Match:
    def __init__(self, team_home, team_away):
        self.team_home = team_home
        self.team_away = team_away
        self.field_factor = 10

    def match(self):
        self.team_home.matches += 1
        self.team_away.matches += 1
        goals_home = 0
        goals_away = 0
        '''
        if abs(self.team_home.force - self.team_away.force) > 40 and random.randint(0, 100) < 20:
            for _ in range(3):
                shot_home = random.randint(0, 100)
                shot_away = random.randint(0, 100)
                if shot_home < 50:
                    goals_home += 1
                if shot_away < 50:
                    goals_away += 1
            # print(self.team_home.name, goals_home, "-", goals_away, self.team_away.name)
        '''
        if True:
            for _ in range(4):
                dec = (self.team_home.force * self.team_away.force) / (self.team_home.force + self.team_away.force)
                home_sf = (self.team_home.force + self.field_factor - dec * (self.team_home.force / 100))
                away_sf = (self.team_away.force - dec * (self.team_away.force / 100))
                shot_home = random.randint(int((goals_home / 4) * home_sf), 100)
                shot_away = random.randint(int((goals_home / 4) * away_sf), 100)
                if shot_home < home_sf:
                    goals_home += 1
                if shot_away < away_sf:
                    goals_away += 1
            self.team_home.goals_scored += goals_home
            self.team_away.goals_scored += goals_away
            self.team_home.goals_conceded += goals_away
            self.team_away.goals_conceded += goals_home
        if goals_home > goals_away:
            # if self.team_home.name == "Fiorentina" or self.team_away.name == "Fiorentina":
            # print(self.team_home.name, goals_home, "-", goals_away, self.team_away.name)
            # print(self.team_home.name, "winner")
            self.team_home.wins += 1
            self.team_home.points += 3
            self.team_away.losses += 1
            return 1
        elif goals_home < goals_away:
            # if self.team_home.name == "Fiorentina" or self.team_away.name == "Fiorentina":
            # print(self.team_home.name, goals_home, "-", goals_away, self.team_away.name)
            # print(self.team_away.name, "winner")
            self.team_away.wins += 1
            self.team_away.points += 3
            self.team_home.losses += 1
            return 2
        elif goals_home == goals_away:
            # if self.team_home.name == "Fiorentina" or self.team_away.name == "Fiorentina":
            # print(self.team_home.name, goals_home, "-", goals_away, self.team_away.name)
            # print("Draw!")
            self.team_home.draws += 1
            self.team_away.draws += 1
            self.team_home.points += 1
            self.team_away.points += 1
            return 0


class SerieA:
    def __init__(self):
        Inter = Team(91, "Inter")
        Milan = Team(79, "Milan")
        Atalanta = Team(78, "Atalanta")
        Juventus = Team(78, "Juventus")
        Napoli = Team(77, "Napoli")
        Lazio = Team(68, "Lazio")
        Fiorentina = Team(65, "Fiorentina")
        Roma = Team(62, "Roma")
        Sassuolo = Team(62, "Sassuolo")
        Sampdoria = Team(52, "Sampdoria")
        Verona = Team(45, "Verona")
        Genoa = Team(42, "Genoa")
        Bologna = Team(41, "Bologna")
        Udinese = Team(40, "Udinese")
        Spezia = Team(39, "Spezia")
        Cagliari = Team(37, "Cagliari")
        Torino = Team(37, "Torino")
        Benevento = Team(33, "Benevento")
        Crotone = Team(23, "Crotone")
        Parma = Team(20, "Parma")
        self.teams = [Inter, Milan, Atalanta, Juventus, Napoli, Lazio, Fiorentina, Roma, Sassuolo, Sampdoria, Verona,
                      Genoa,
                      Bologna, Udinese, Spezia, Cagliari, Torino, Benevento, Crotone, Parma]

    def remove_team(self, team):
        self.teams.remove(team)

    def add_team(self, team):
        self.teams.append(team)


class SerieB:
    def __init__(self):
        Empoli = Team(73, "Empoli")
        Salernitana = Team(69, "Salernitana")
        Monza = Team(64, "Monza")
        Lecce = Team(62, "Lecce")
        Venezia = Team(59, "Venezia")
        Cittadella = Team(57, "Cittadella")
        Brescia = Team(56, "Brescia")
        Chievo = Team(56, "Chievo")
        SPAL = Team(56, "SPAL")
        Frosinone = Team(50, "Frosinone")
        Reggina = Team(50, "Reggina")
        Vicenza = Team(48, "Vicenza")
        Cremonese = Team(48, "Cremonese")
        Pisa = Team(48, "Pisa")
        Pordenone = Team(45, "Pordenone")
        Ascoli = Team(44, "Ascoli")
        Cosenza = Team(35, "Cosenza")
        Reggiana = Team(34, "Reggiana")
        Pescara = Team(32, "Pescara")
        Virtus_Entella = Team(23, "Virtus_Entella")
        self.teams = [Empoli, Salernitana, Monza, Lecce, Venezia, Cittadella, Brescia, Chievo, SPAL, Frosinone,
                      Reggina, Vicenza, Cremonese, Pisa, Pordenone, Ascoli, Cosenza, Reggiana, Pescara,
                      Virtus_Entella]

    def remove_team(self, team):
        self.teams.remove(team)

    def add_team(self, team):
        self.teams.append(team)


def league(serie_1, serie_2):
    # TEAM_1
    # creating schedule
    for j in range(38):
        teams1 = serie_1.teams[:]
        for i in range(10):
            home = teams1[schedule[j][i][0] - 1]
            away = teams1[schedule[j][i][1] - 1]
            Match(home, away).match()

    teams1 = serie_1.teams[:]
    # sorting standings
    teams1.sort(reverse=True, key=Team.get_points)

    print("    Team\t\t", "Points\t", "Wins\t", "Draws\t", "Losses\t", "Matches\t", "GS\t", "GC\t", "Force")
    for i in range(20):
        teams1[i].history.append([i + 1, "A"])
        if i < 4:
            print(
                f"{i + 1:<3} {Fore.GREEN}{teams1[i].name:<13}{Style.RESET_ALL} {teams1[i].points:<6} {teams1[i].wins:<8} {teams1[i].draws:<8} "
                f"{teams1[i].losses:<7} {teams1[i].matches:<7} {teams1[i].goals_scored:<3} {teams1[i].goals_conceded:<5} "
                f"{teams1[i].force:<5}")
        elif i < 6:
            print(
                f"{i + 1:<3} {Fore.YELLOW}{teams1[i].name:<13}{Style.RESET_ALL} {teams1[i].points:<6} {teams1[i].wins:<8} {teams1[i].draws:<8} "
                f"{teams1[i].losses:<7} {teams1[i].matches:<7} {teams1[i].goals_scored:<3} {teams1[i].goals_conceded:<5} "
                f"{teams1[i].force:<5}")
        elif i > 16:
            print(
                f"{i + 1:<3} {Fore.RED}{teams1[i].name:<13}{Style.RESET_ALL} {teams1[i].points:<6} {teams1[i].wins:<8} {teams1[i].draws:<8} "
                f"{teams1[i].losses:<7} {teams1[i].matches:<7} {teams1[i].goals_scored:<3} {teams1[i].goals_conceded:<5} "
                f"{teams1[i].force:<5}")
        else:
            print(
                f"{i + 1:<3} {teams1[i].name:<14}{teams1[i].points:<6} {teams1[i].wins:<8} {teams1[i].draws:<8} "
                f"{teams1[i].losses:<7} {teams1[i].matches:<7} {teams1[i].goals_scored:<3} {teams1[i].goals_conceded:<5} "
                f"{teams1[i].force:<5}")

    # updating teams stats
    for i in range(20):
        teams1[i].force = teams1[i].get_points()
        teams1[i].reset()

    print()

    # TEAM_2
    # creating schedule
    for j in range(38):
        teams2 = serie_2.teams[:]
        for i in range(10):
            home = teams2[schedule[j][i][0] - 1]
            away = teams2[schedule[j][i][1] - 1]
            Match(home, away).match()

    teams2 = serie_2.teams[:]
    # sorting standings
    teams2.sort(reverse=True, key=Team.get_points)

    print("    Team\t\t", "Points\t", "Wins\t", "Draws\t", "Losses\t", "Matches\t", "GS\t", "GC\t", "Force")
    for i in range(20):
        teams2[i].history.append([(i + 1) + 20, "B"])
        print(f"{i + 1:<3} {teams2[i].name:<14} {teams2[i].points:<6} {teams2[i].wins:<8} {teams2[i].draws:<8} "
              f"{teams2[i].losses:<7} {teams2[i].matches:<7} {teams2[i].goals_scored:<3} {teams2[i].goals_conceded:<5} "
              f"{teams2[i].force:<5}")

    # updating teams stats
    for i in range(20):
        teams2[i].force = teams2[i].get_points()
        teams2[i].reset()

    # swapping standings
    for i in range(3):
        team_to_remove = teams1.pop()
        team_to_remove.force *= 3
        serie_1.remove_team(team_to_remove)
        serie_2.add_team(team_to_remove)

    for i in range(3):
        team_to_remove = teams2.pop(0)
        team_to_remove.force /= 3
        serie_2.remove_team(team_to_remove)
        serie_1.add_team(team_to_remove)

    random.shuffle(serie_1.teams)
    random.shuffle(serie_2.teams)

    print()
    print()


if __name__ == '__main__':

    '''
    model = Model("/Users/andrealeonardo/Documents/Uni/Calendar/calendar.mzn")
    solver = Solver.lookup("chuffed")
    instance = Instance(solver, model)
    instance["S"] = 20
    result = instance.solve(timeout=timedelta(minutes=20))
    calendar = result["calendario"]
    # print(calendar)
    printCalendario(calendar)

    json_cal = json.dumps(calendar)

    with open('json_cal.json', 'w') as outfile:
        outfile.write(json_cal)
    '''

    with open('json_cal.json') as json_file:
        schedule = json.load(json_file)

    for i in range(19):
        g = []
        for j in range(10):
            g.append([schedule[i][j][1], schedule[i][j][0]])
        schedule.append(g)

    serie_a = SerieA()
    serie_b = SerieB()
    years = 100
    for i in range(years):
        league(serie_a, serie_b)

    h = []
    for s in serie_a.teams:
        if s.name == "Fiorentina":
            h = s.history
    for s in serie_b.teams:
        if s.name == "Fiorentina":
            h = s.history

    x = [i for i in range(years)]
    y = [h[i][0] for i in range(years)]
    #c = ['red' if yy > 20 else 'blue' for yy in y]

    plt.plot(x,y)

    XB = []
    XA = []
    YB = []
    YA = []
    for i in range(len(x)):
        if y[i] > 20:
            XB.append(x[i])
            YB.append(y[i])
        else:
            XA.append(x[i])
            YA.append(y[i])

    plt.scatter(XB,YB, color='red', s=10)
    plt.scatter(XA,YA, color='blue',s=10)
    plt.gca().invert_yaxis()
    plt.show()
