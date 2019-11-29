# Sprint 2

## Executive summary - Sprint 1

### Josef

Jag har jobbat med att sätta upp servern inför sprint 1. Vi använde den virtuella maskinen tillhandahållen av LUDD, där vi satt upp mySql som databas, en flask-applikation för att kommunicera med backenden samt Nginx för att komma åt sidan via vår statiska IP.

Jag har även experimenterat med att interagera med mySql, främst på min egen maskin för enkelhetens skull, men sett till så att allt är kompatibelt för att emigrera till den virtuella maskinen.

### Leo

Jag har tillsammans med Josef tagit fram user stories samt gjort en enkel hemsida med html och css. 

## Executive summary - Sprint 2

### Josef

Jag har byggt om databasen för att hantera produkter, kategorier och användare mm. Jag har även lagt till strukturen för orderhantering i databasen, i form av ett orders-table och et orderItem-table. En grundläggande managin har också lagts till.

# Userstories

## Admin

1. Har alla rättigheter som manager.
2. Kan ändra rättigheter för alla användare på sidan.
3. Kan lägga till och radera
	+ Kategorier
	+ Tagtyper

## Manager

1. Har alla rättigheter som en inloggad användare.
2. Kan öppna en manager meny.
3. Har tillgång till att redigera alla
  + Användare
  + Produkter
  + Kategorier 
  + Tagtyper
  + Reviews
  + Carts
  + Orders

4. Kan få en lista med alla ordrar i manager-menyn, där man ser betalade ordrar samt hanterade ordrar separat
5. Kan lägga till och radera
  + Användare
  + Produkter
  + Taggar
  
## Inloggad användare

1. Har alla rättigheter som en icke inloggad användare.
2. Kan orientera sig mellan kategorier till produkter.
3. Kan lägga produkter i sin kundvagn.
4. Kan öppna sin kundvagn och se vad som ligger i.
5. Kan lägga en order som senare hanteras av managers.
6. Kan logga ut från sin användare.

## Icke inloggad användare

2. Kan orientera sig mellan kategorier till produkter.
3. Kan logga in, eller skapa en användare.

# Nuvarande Backlog

![](https://snipboard.io/VsZz31.jpg)

# ER-diagram

![](https://snipboard.io/Q965AY.jpg)

# Kodbas

Koden finns tillgänglig publikt på Github under min användare (JosefUtbult). Där ligger även backloggen i form av issues.
``` https://github.com/JosefUtbult/Musikdong/```

# Tester

## Icke inloggad användare

### Hitta en produkt

1. Öppna startsida
2. Navigera till en kategori.
3. Navigera till en produkt.
4. Öppna sida för produkt.

### Skapa användare

1. Tryck på _Sign Up_.
2. Välj ett användarnamn.
	+ Det ska inte gå att välja ett användarnamn som redan är registrerad.
3. Välj lösenord.
4. Skapa användare.

### Logga in

1. Tryck på _Login_.
2. Skriv in användarnamn och lösenord.
3. Logga in.

## Inloggad användare

### Lägg vara i kundvagn

1. Navigera till en vara.
2. Lägg i kundvagn.

### Visa kundvagn

1. Tryck på kundvagn i headern

### Lägg order

1. Öppna kundvagnen
2. Lägg order

## Manager

### Visa produkt/användare/ordrar

1. Tryck på _Manager_ i headern.
2. Navigera till produkt/användare/ordrar
3. Öppna sida för produkt/användare/ordrar

### Redigera produkt/användare/ordrar

1. Navigera till produkt/användare/ordrar
2. Redigera produkt/kategori/ordrar
3. Tryck på _Update_

### Redigera produkt/användare/ordrar

1. Öppna _Manager_.
2. Tryck på _Add_
3. Fyll i produkt/användare/ordrar
4. Tryck på _Add_.

### Radera produkt/användare/ordrar

1. Navigera till produkt/användare/ordrar
2. Redigera produkt/användare/ordrar
3. Tryck på _Delete_

## Admin

### Updatera tagtyp/kategori/rättigheter produkt/användare/ordrar
1. Utförs på samma sätt som produkt/användare/ordrar

### Radera tagtyp/kategor
1. Utförs på samma sätt som produkt/användare/ordrar

# Limitations
 Säkerhet
  + Flask kör på en öppen ip
  + MySQL är öppen för remote login
  + Mycket går att ta sig runt
* Kundvagn
  + Kundvagnen kan bara hålla en enhet av en produkt för en användare. Orderitems har däremot ett antal.
