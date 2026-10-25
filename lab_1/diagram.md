# UML-диаграмма классов

~~~mermaid
classDiagram
    DataReader <|-- TextDataReader
    DataReader <|-- YamlDataReader

    class DataReader {
        <<abstract>>
        +read(path) DataType
    }

    class TextDataReader {
        +read(path) DataType
    }

    class YamlDataReader {
        +read(path) DataType
    }

    class CalcRating {
        +data
        +calc() dict
    }

    class CalcExcellent {
        +data
        +calc() int
    }
~~~
