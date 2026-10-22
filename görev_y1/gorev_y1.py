import math
import matplotlib.pyplot as plt
def distance(lat1, lat2, lon1, lon2):
    try:
        lat1, lon1, lat2, lon2 = float(lat1), float(lon1), float(lat2), float(lon2)
        if not (-90 <= lat1 <= 90 and -90 <= lat2 <= 90):
           raise ValueError("Enlem değerleri -90 ile 90 arasinda olmalıdır")

        if not (-180 <= lon1 <= 180 and -180 <= lon2 <= 180):
            raise ValueError("Boylam değerleri -180 ile 180 arasında olmalıdır")
        
        print("koordinatlar geçerli")

        phi1= math.radians(lat1) 
        phi2=math.radians(lat2)
        lambda1=math.radians(lon1)
        lambda2=math.radians(lon2)

        differencephi= phi2 - phi1
        differencelambda = lambda2 - lambda1

        a = math.sin(differencephi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(differencelambda/2)**2
        c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))
        R= 6371000
        distance_value= R*c

        return(distance_value)

    except ValueError:
        print("yanlış koordinat girişi:{ValueError}")
        return None
dist1=distance(39.8860,39.8925,32.7810,32.7905)
dist2=distance(39.8925,39.8800,32.7905,32.7950)
real_distance= dist1+dist2

def bearing(lat1,lat2,lon1,lon2):
    phi1= math.radians(lat1) 
    phi2=math.radians(lat2)
    lambda1=math.radians(lon1)
    lambda2=math.radians(lon2)
    differencephi= phi2 - phi1
    differencelambda = lambda2 - lambda1

    x=math.sin(differencelambda)*math.cos(phi2)
    y = math.cos(phi1)*math.sin(phi2)- math.sin(phi1)*math.cos(phi2)

    b=math.atan2(x,y)
    bearing_deg=math.degrees(b)
    return(bearing_deg+360) %360
bearing1=bearing(39.8860, 39.8925, 32.7810, 32.7905)
bearing2=bearing(39.8925, 39.8800, 32.7905, 32.7950)
print(f"A -> B | Mesafe: {dist1:.2f} m | Yön: {bearing1:.2f}°")
print(f"B -> C | Mesafe: {dist2:.2f} m | Yön: {bearing2:.2f}°")
print(f"Toplam Rota: {real_distance:.2f} metre")

    
                