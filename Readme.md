# CONTROL DE CADUCIDADES

El programa de control de caducidades permite dar de alta
artículos con diferentes características, entre ellas,
un stock asociado a un lote y una fecha, y una fecha de caducidad.

Se realizarán recuentos diarios de las unidades en stock
de cada producto y se registrarán en una base de datos.

El programa permite consultar y manejar las unidades próximas a la 
caducidad registrada, así como las unidades caducadas.

## Requisitos

El programa debe incluir programación de objetos, bases de datos,
librerías y la utilización de un framework

## Objetivo

El objetivo de este proyecto es superar el proyecto de fin de curso
para obtener el título "Programación Pyhton"

## Diseno

```mermaid
sequenceDiagram
    participant A as Alice
    participant J as John
    A->>J: Hello John, how are you?
    J->>A: Great!
```

#Probando UML

### uml: class diagram
```plantuml
@startuml
package "customer domain" #DDDDDD {
    class Contact {
        + email
        + phone
    }

    class Address {
        + address1
        + address2
        + city
        + region
        + country
        + postalCode
        + organization
    }

    note right of Address 
        There are two types of 
        addresses: billing and shipping
    end note

    class Customer {
    }

    Customer *-- Contact
    Customer *-- ShippingAddress
    Customer *-- BillingAddress
    Customer *--{ SalesOrder

    class ShippingAddress <<Address>>
    class BillingAddress <<Address>>
    class SalesOrder {
        + itemDescription
        + itemPrice
        + shippingCost
        + trackingNumber
        + shipDate
    }
}
@enduml
```

## Construido con

-Python

-Framwork (definir)

-SQLite
