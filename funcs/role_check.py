from settings.settings import admin_roles
import nextcord

def check_for_admin(ctx):
    flag = 0
    for role in admin_roles:
        if nextcord.utils.get(ctx.author.roles, name=role):
            print(f"{role} found in {ctx.author.name} ranks")
            flag = 1
        else:
            print(f"{role} not found in {ctx.author.name} ranks")
    if flag == 1:
        return True
    else:
        return False
