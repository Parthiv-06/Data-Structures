def trapping_rain_water(a):
    left_max=0
    right_max=0
    l=0
    r=len(a)-1
    total_water=0
    while l<r:
        if a[l]<=a[r]:
            if a[l]<left_max:
                total_water+=left_max-a[l]
            left_max=max(a[l],left_max)
            l+=1
        else:
            if a[r]<right_max:
                total_water+=right_max-a[r]
            right_max=max(right_max,a[r])
            r-=1
    return total_water
a=[0,1,0,2,1,0,1,3,2,1,2,1]
print(trapping_rain_water(a))
