import math
OV = 1.05                      # assumed 3-way overround
fair_p = lambda o: (1/o)/OV    # vig-removed true probability of a book price

def plan(rung, p_rung, start=100.0, target=3000.0):
    """Full rungs at `rung`, then one exact-landing final rung."""
    n = math.floor(math.log(target/start)/math.log(rung))
    bank = start*rung**n
    last = target/bank                       # exact odds needed on the final rung
    P = (p_rung**n) * fair_p(last)
    return n, last, P, P*target

print("$100 -> $3,000, final rung sized to land EXACTLY on target")
print(f"{'structure':34} {'rung':>5} {'full':>5} {'final':>6} {'legs':>5} {'P(win)':>8} {'EV':>8}")
rows = [
 ("2-leg: Stuttgart x Arsenal",  1.22*1.75, fair_p(1.22)*fair_p(1.75), 2),
 ("2-leg: Stuttgart x Liverpool",1.22*1.73, fair_p(1.22)*fair_p(1.73), 2),
 ("2-leg: Arsenal x Liverpool",  1.75*1.73, fair_p(1.75)*fair_p(1.73), 2),
 ("2-leg: Barca x Stuttgart",    1.05*1.22, fair_p(1.05)*fair_p(1.22), 2),
 ("1-leg singles @ 1.75",        1.75,      fair_p(1.75),              1),
 ("1-leg singles @ 1.22",        1.22,      fair_p(1.22),              1),
]
best=None
for name, ro, pr, nl in rows:
    n, last, P, ev = plan(ro, pr)
    legs = n*nl + 1
    print(f"{name:34} {ro:5.2f} {n:5d} {last:6.3f} {legs:5d} {P*100:7.2f}% ${ev:7.2f}")

print("\nRECOMMENDED PATH — 4 full rungs of (Stuttgart x Arsenal), then one single")
rung = 1.22*1.75
pr   = fair_p(1.22)*fair_p(1.75)
bank = 100.0
for i in range(1,5):
    nxt = bank*rung
    print(f"  rung {i}: stake ${bank:8.2f}  @ {rung:.3f}  ->  ${nxt:8.2f}")
    bank = nxt
last = 3000/bank
print(f"  rung 5: stake ${bank:8.2f}  @ {last:.3f} (SINGLE) ->  $3000.00")
P = pr**4 * fair_p(last)
print(f"\n  P(complete) = {P*100:.2f}%   ->  1 in {1/P:.0f}")
print(f"  P(bust)     = {(1-P)*100:.2f}%")
print(f"  EV          = ${P*3000:.2f} on $100 staked ({(P*3000/100-1)*100:+.1f}%)")
print(f"  P(survive rung 1 only) = {pr*100:.1f}%")
