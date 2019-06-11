from random import *


def log(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")


def server_joined(member):
    x = randint(1, 2)
    if x == 1:
        return ('**Et bienvenue à <@' + str(member.id) + '> qui rentre à 110 km/h dans le serveur '
                                                         'au volant de son EBR 105**')
    elif x == 2:
        return '**Et c\'est <@' + str(member.id) + '> qui arrive, SCAR en main, près à faire un Top 1**'


def server_left(member):
    y = randint(1, 3)
    if y == 1:
        return '**Au revoir à ' + member.name + ' (<@' + str(member.id) + '>) qui a ragequit après s\'être fait ' \
                              'ammorack par un Tog II**'
    if y == 2:
        return '**Au revoir à ' + member.name + ' (<@' + str(member.id) + '>) qui part afin de devenir joueur ' \
                              'professionnel de Tetris 99 Battle Royale**'
    if y == 3:
        return '**Au revoir à ' + member.name + ' (<@' + str(member.id) + '>) qui ne reviendra pas, car il a jeté' \
                              ' son pc par la fenètre après s\'etre fait one shot par l\'arty**'


def code():
    code_message = "Procédure d'utilisation d'un code Wargaming\n" \
           "→ allez sur ce lien: https://eu.wargaming.net/shop/redeem/\n" \
           "→ connectez-vous avec votre compte Wargaming si ce n'est pas déjà fait\n" \
           "→ entrez le code dans la zone prévu à cet effet\n" \
           ":warning: si le code ne marche pas, cela signifie que le site est momentanément " \
           "surchargé, que le code ne marche plus ou n'a jamais marché"
    return code_message


def help():
    help_message = "```\n" \
                   "$help            Pour avoir de l'aide sur les fonctionnalités du bot\n" \
                   "$code            Pour savoir comment utiliser un code Wargaming\n" \
                   "``` "
    return help_message

