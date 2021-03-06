"""
    DEFAULT TEXT MESSAGES TO BE DISPLAYED SHALL BE DEFINED HERE TO AVOID TEXT CLUTTERING
"""

help_txt = '\t\t\t\tG.O.D.A' \
           '\n\t\t\t\t( ͡° ͜ʖ ͡°)' \
           '\n\t• GENERIC\n\t• OBJECTIVE\n\t• DATA\n\t• ADMINISTRATOR' \
           '\n\t------------------------------------' \
           '\n\tVERSION\t\t\t\t1.0' \
           '\n\tRELEASE DATE\t\t05-15-2018' \
           '\n\tWEBSITE\t\t\t\thttps://icom4036.github.io/GODA' \
           '\n\tREPOSITORY\t\t\thttps://github.com/ICOM4036/GODA'\
           '\n\t------------------------------------' \
           '\n\nFOR MORE INFORMATION ON A COMMAND TYPE "HELP [CMD]"\n' \
           '\nQUIT\t\t\tEXIT THE PROGRAM OR CLOSE AN ACTIVE LIBRARY' \
           '\nOPEN\t\t\tOPEN AN EXISTING LIBRARY' \
           '\nCRT\t\t\t\tCREATE LIBRARY, COLLECTION, INSTANCE OF AN OBJECT, OR OBJECT DEFINITION' \
           '\nSHOW\t\t\tDISPLAY LIBRARY, COLLECTION, OR ALL ACTIVE LIBRARIES' \
           '\nRM\t\t\t\tREMOVE A LIBRARY, COLLECTION, INSTANCE OF AN OBJECT' \
           '\nSORT\t\t\tSORT A COLLECTION BY A SPECIFIC ATTRIBUTE' \
           '\nMERGE\t\t\tMERGE TWO EXISTING COLLECTIONS INTO A NEW ONE, WHERE THE FIRST ONE APPEARS BEFORE THE SECOND IN THE NEW COLLECTION' \
           '\nSEARCH\t\t\tSEARCH IN A COLLECTION ALL OBJECT DEFINITIONS FOR A SPECIFIC ATTRIBUTE' \
           '\nIMP\t\t\t\tIMPORT LIBRARY, COLLECTION OR COMMAND' \
           '\nEXP\t\t\t\tEXPORT COLLECTION OR LIBRARY TO THE USERS DESKTOP' \
           '\nRUN\t\t\t\tRUN AN IMPORTED COMMAND. TYPE "HELP RUN" TO SEE LIST OF IMPORTED COMMANDS. ' \

help_cmd = {
    'open': '\nOPEN LIB\t\tOPENS A LIBRARY INSTANCE',

    'quit': '\nQUIT\t\tEXIT THE PROGRAM'
            '\nQUIT LIB\t\tCLOSE AN OPENED LIBRARY',

    'crt': '\nCRT LIB\t\tCREATE LIBRARY'
            '\nCRT COL\t\tCREATE COLLECTION'
            '\nCRT OBJ\t\tCREATE OBJECT'
            '\nCRT INST\t\tADD AN INSTANCE OF AN OBJECT TO A COLLECTION',

    'show': '\nSHOW LIB\t\tDISPLAY COLLECTIONS THAT BELONG TO A LIBRARY'
            '\nSHOW COL\t\tDISPLAY EVERYTHING INSIDE A COLLECTION'
            '\nSHOW ALL\t\tDISPLAY EVERYTHING INSIDE EVERY COLLECTION OF A LIBRARY',

    'rm': '\nRM LIB\t\tREMOVE A LIBRARY'
          '\nRM COL\t\tREMOVE A COLLECTION'
          '\nRM INST\t\tREMOVE AN INSTANCE FROM A COLLECTION',

    'imp': '\nIMP LIB\t\tIMPORT A LIBRARY'
           '\nIMP COL\t\tIMPORT A COLLECTION'
           '\nIMP CMD\t\tIMPORT A COMMAND',

    'exp': '\nEXP LIB\t\tEXPORT A LIBRARY'
           '\nEXP COL\t\tEXPORT A COLLECTION',

    'sort': '\nSORT\t\tSORT A COLLECTION BY A SPECIFIC ATTRIBUTE',

    'merge': '\nMERGE\t\tMERGE TWO COLLECTIONS INTO ONE',

    'search': '\nSEARCH\t\tSEARCH IN A COLLECTION A SPECIFIC ATTRIBUTE'
}