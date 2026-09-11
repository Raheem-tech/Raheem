import math
# --- Sat 12 Sep 2026, verified three-way prices ---
# Sunderland v Arsenal: 6.91 / 4.21 / 1.46
ars_imp, dr, sun = 1/1.46, 1/4.21, 1/6.91
ov_ars = ars_imp+dr+sun
p_ars = ars_imp/ov_ars
# Liverpool v Fulham: only the 1.44 favourite price verified; assume same overround
p_liv = (1/1.44)/ov_ars

print(f"Sunderland v Arsenal book overround: {ov_ars*100:.2f}%")
print(f"  Arsenal   1.46  implied {ars_imp*100:.1f}%  fair {p_ars*100:.1f}%  fair odds {1/p_ars:.2f}")
print(f"  Liverpool 1.44  implied {1/1.44*100:.1f}%  fair {p_liv*100:.1f}%  fair odds {1/p_liv:.2f}")

rung = 1.46*1.44
p    = p_ars*p_liv
print(f"\nRUNG 2: Arsenal x Liverpool = {rung:.3f}")
print(f"  true probability {p*100:.1f}%   fair price {1/p:.3f}")
print(f"  value received   {rung*p*100:.1f}% of fair  ({(rung*p-1)*100:+.1f}%)")
print(f"  (rung 1 was 42.5% @ -9.3%)")

bank = 213.50
after = bank*rung
print(f"\n  ${bank:.2f} -> ${after:.2f}")

# remaining ladder from after rung 2
n = math.floor(math.log(3000/after)/math.log(rung))
mid = after*rung**n
last = 3000/mid
P_rest = p**n * ((1/last)/ov_ars)
print(f"\nREMAINING after rung 2: {n} full rungs @ {rung:.3f} + final single @ {last:.3f}")
b=after
for i in range(n):
    b*=rung; print(f"   rung {3+i}: -> ${b:.2f}")
print(f"   rung {3+n}: single @ {last:.3f} -> $3000.00")

P_now  = p * P_rest
print(f"\nP(complete from ${bank:.2f} today) = {P_now*100:.2f}%  (1 in {1/P_now:.0f})")
print(f"P(survive rung 2 alone)          = {p*100:.1f}%")
print(f"EV of the whole remaining path   = ${P_now*3000:.2f} on ${bank:.2f} at risk ({(P_now*3000/bank-1)*100:+.1f}%)")
