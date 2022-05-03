import random
import json

with open('json_cal.json') as json_file:
    schedule = json.load(json_file)

for i in range(19):
    g = []
    for j in range(10):
        g.append([schedule[i][j][1], schedule[i][j][0]])
    schedule.append(g)


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
        if abs(self.team_home.force - self.team_away.force) > 40 and random.randint(0, 100) < 20:
            for _ in range(3):
                shot_home = random.randint(0, 100)
                shot_away = random.randint(0, 100)
                if shot_home < 50:
                    goals_home += 1
                if shot_away < 50:
                    goals_away += 1
            # print(self.team_home.name, goals_home, "-", goals_away, self.team_away.name)
        else:
            for _ in range(5):
                shot_home = random.randint(0, 100)
                shot_away = random.randint(0, 100)
                if shot_home < (self.team_home.force + self.field_factor):
                    goals_home += 1
                if shot_away < self.team_away.force:
                    goals_away += 1
            self.team_home.goals_scored += goals_home
            self.team_away.goals_scored += goals_away
            self.team_home.goals_conceded += goals_away
            self.team_away.goals_conceded += goals_home
        if goals_home > goals_away:
            # print(self.team_home.name, goals_home, "-", goals_away, self.team_away.name)
            # print(self.team_home.name, "winner")
            self.team_home.wins += 1
            self.team_home.points += 3
            self.team_away.losses += 1
            return 1
        elif goals_home < goals_away:
            # print(self.team_home.name, goals_home, "-", goals_away, self.team_away.name)
            # print(self.team_away.name, "winner")
            self.team_away.wins += 1
            self.team_away.points += 3
            self.team_home.losses += 1
            return 2
        elif goals_home == goals_away:
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
        Roma = Team(62, "Roma")
        Sassuolo = Team(62, "Sassuolo")
        Sampdoria = Team(52, "Sampdoria")
        Verona = Team(45, "Verona")
        Genoa = Team(42, "Genoa")
        Bologna = Team(41, "Bologna")
        Fiorentina = Team(40, "Fiorentina")
        Udinese = Team(40, "Udinese")
        Spezia = Team(39, "Spezia")
        Cagliari = Team(37, "Cagliari")
        Torino = Team(37, "Torino")
        Benevento = Team(33, "Benevento")
        Crotone = Team(23, "Crotone")
        Parma = Team(20, "Parma")
        self.teams = [Inter, Milan, Atalanta, Juventus, Napoli, Lazio, Roma, Sassuolo, Sampdoria, Verona, Genoa,
                       Bologna, Fiorentina, Udinese, Spezia, Cagliari, Torino, Benevento, Crotone, Parma]

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
                       Reggina, Vicenza, Cremonese, Pisa, Pordenone, Ascoli, Cosenza, Reggiana, Pescara, Virtus_Entella]

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
        print(f"{i + 1:<3} {teams1[i].name:<14} {teams1[i].points:<6} {teams1[i].wins:<8} {teams1[i].draws:<8} "
              f"{teams1[i].losses:<7} {teams1[i].matches:<9} {teams1[i].goals_scored:<3} {teams1[i].goals_conceded:<5} "
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
        print(f"{i+1:<3} {teams2[i].name:<14} {teams2[i].points:<6} {teams2[i].wins:<8} {teams2[i].draws:<8} "
              f"{teams2[i].losses:<7} {teams2[i].matches:<9} {teams2[i].goals_scored:<3} {teams2[i].goals_conceded:<5} "
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


serie_a = SerieA()
serie_b = SerieB()
for i in range(10):
    league(serie_a, serie_b)


def printGiornata(g, i):
    print("GIORNATA ", i)

    for scontro in g:
        print(serie_a.teams[scontro[0] - 1].name + " - " + serie_a.teams[scontro[1] - 1].name)


def printCalendario(c):
    print("CALENDARIO:")
    i = 1
    for giornata in c:
        printGiornata(giornata, i)
        i = i + 1
        print("\n")


# printCalendario(schedule)
