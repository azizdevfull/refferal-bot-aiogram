users = {
    "1234": {"reffer_id": "5678", "flag": True},
    "1235": {"reffer_id": "5678", "flag": True},
    "5678": {"reffer_id": None, "flag": True},
    "1237": {"reffer_id": "5678", "flag": True},
    "1238": {"reffer_id": "5678", "flag": True},
    "1239": {"reffer_id": "5678", "flag": True}
}
def get_user_ball(user_id):
        ball = 0
        for user in users.values():
            if user_id == user['reffer_id'] and user['flag']: ball += 1
        # print(f"{user} => {ball} ball")
        return ball