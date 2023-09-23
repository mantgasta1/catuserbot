from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 20281694
    API_HASH = "c6a82571e07c6eb55f38d1c3b3c28de6"
    # the name to display in your alive message
    ALIVE_NAME = "𝑬𝒉𝒔𝒂𝒏 𝑷𝑪 ◔"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://mdzxqnxe:SJ3_YndgBBQnPYrINrFyYFf5MrSrxCcd@lallah.db.elephantsql.com/mdzxqnxe"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BJWap1wBuymGZdjKwn2nFrcLL8o34ybGtCMRnwmaAMIReBN2KsqzibLuKsohk5rtE24q0nGLWGBUpmkI36gfypzDS_7wi_d_ittb1tQ1zmdUyZeCnZ7KMRqjDAfQF_ExjI-E1mCxhV0_TtW443sU7lqKTUVQoGYYKchBjdFCXnf1u31qV-pb4kFS3p6Gh87at237XwTzqATFQGWrevHGnG-g0ipcsCBCoQ1YrHS0GeVesfdAkrpikumDqPI569gMh6doeb32TaC8mytwMvkjnDEV2zop0_RBQHKLq5zyuXTNduA4rrPI5IqN_5NNMSS0jRve_3_rp7wVeDyugf4zLZJVtowgZgo="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6548277654:AAF6XFuJgfZjsEQqVRBB11RM1kzEI5gz-2g"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -4050627371
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
