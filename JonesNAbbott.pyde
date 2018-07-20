def setup():
    size(500, 700)
    background(200,50,70)
    Title = "Jones N Abbotts"
    f = loadFont("Papyrus-Regular-48.vlw")
    textFont(f)
    textSize(35)
    text(Title, 110, 50) 
    
    text("Appetizers", 160, 115)
    
    appetizers = {"Fried Mozzarella":5.99,
    "Spicy Shrimp Scampi Fritta":9.49,
    "Stuffed Mushrooms":7.99, 
    "Spinach Artichoke Dip":8.29,
    "Sweet Chilli Shrimp":9.79,}
    
    appnum = 0
    textSize(20)
    for i in appetizers:
        while appnum <= 5:
            text(appetizers[i], 160, 145)
            appnum = appnum + 1
