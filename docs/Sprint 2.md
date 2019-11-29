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
1. Kan öppna en manager meny.
2. Har tillgång till att redigera alla
  + Användare
  + Produkter
  + Kategorier 
  + Tagtyper
  + Reviews
  + Carts
  + Orders

3. Kan få en lista med alla ordrar i manager-menyn, där man ser betalade ordrar samt hanterade ordrar separat
4. Kan lägga till och radera
  + Användare
  + Produkter
  + Taggar
