import shelve

fn = 'v:\workspace\Python2_Homework04\src\scoreboard_fixture.shlf'
             
def highscore(player, score):
    scoretable = shelve.open(fn, writeback=True)
    
    if player not in scoretable:
        scoretable[player] = stored_score = score
    else:
        stored_score = scoretable[player]
        if score > stored_score:
            scoretable[player] = stored_score = score
        
    scoretable.close()
    return stored_score