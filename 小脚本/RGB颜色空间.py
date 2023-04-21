def linear_sRGB(c):
    if c <= 0.04045:
        return c / 12.92
    else:
        return pow((c + 0.055) / 1.055, 2.4)

def sRGB_to_XYZn(r, g, b):
    Rlin = linear_sRGB(r / 255.0)
    Glin = linear_sRGB(g / 255.0)
    Blin = linear_sRGB(b / 255.0)
    Xn = Rlin * 0.4124 + Glin * 0.3576 + Blin * 0.1805
    Yn = Rlin * 0.2126 + Glin * 0.7152 + Blin * 0.0722
    Zn = Rlin * 0.0193 + Glin * 0.1192 + Blin * 0.9505
    return Xn, Yn, Zn

def gamma_sRGB(c):
    if c <= 0.0031308:
        return 12.92 * c
    else:
        return 1.055 * pow(c, 1/2.4) - 0.055

def XYZn_to_sRGB(Xn, Yn, Zn):
    Rlin = Xn * 3.2406255 + Yn *-1.5372080 + Zn *-0.4986286
    Glin = Xn *-0.9689307 + Yn * 1.8757561 + Zn * 0.0415175
    Blin = Xn * 0.0557101 + Yn *-0.2040211 + Zn * 1.0569959
    R = round(255 * gamma_sRGB(Rlin))
    G = round(255 * gamma_sRGB(Glin))
    B = round(255 * gamma_sRGB(Blin))
    return R, G, B

def linear_AdobeRGB(c):
    if c <= 0.0:
        return 0.0
    return pow(c, 2.19921875)

def AdobeRGB_to_XYZn(R, G, B):
    Rlin = linear_AdobeRGB(R / 255.0)
    Glin = linear_AdobeRGB(G / 255.0)
    Blin = linear_AdobeRGB(B / 255.0)
    Xn = Rlin * 0.57667 + Glin * 0.18556 + Blin * 0.18823
    Yn = Rlin * 0.29734 + Glin * 0.62736 + Blin * 0.07529
    Zn = Rlin * 0.02703 + Glin * 0.07069 + Blin * 0.99134
    return Xn, Yn, Zn

def gamma_AdobeRGB(c):
    if c <= 0.0:
        return 0.0
    return pow(c, 1/2.19921875)

def XYZn_to_AdobeRGB(Xn, Yn, Zn):
    Rlin = Xn * 2.04159 + Yn *-0.56501 + Zn *-0.34473
    Glin = Xn *-0.96924 + Yn * 1.87597 + Zn * 0.04156
    Blin = Xn * 0.01344 + Yn *-0.11836 + Zn * 1.01517
    R = round(255 * gamma_AdobeRGB(Rlin))
    G = round(255 * gamma_AdobeRGB(Glin))
    B = round(255 * gamma_AdobeRGB(Blin))
    return R, G, B

x, y, z = AdobeRGB_to_XYZn(0.004 * 255, 0.000 * 255, 0.002 * 255)
print(x, y, z)
r, g, b = XYZn_to_sRGB(x, y, z)
print(r* 255, g* 255, b* 255)