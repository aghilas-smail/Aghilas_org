package main.scala
import org.apache.spark.SparkContext

object FirstApp {

def main(args: Array[String]) {
val x = "le chemin de ton fichier "
val conf = new SparkConf().setAppName("HelloSpark").setMaster("local")
val sc = new SparkContext(conf)
val y = sc.textFile(x).cache()
val counts = y.flatMap(line => line.spli(" "))
                .map(word => (word, 1))
                .reduceByKey(_ + _)
counts.saveAsTextFile("Le chemin ou tu va sauvegarder ton fichier " + java.util.UUID.randomUUID.toString)
sc.stop()

}}

--------------*

package main.scala
import org.apache.spark.SparkContext

object FirstApp {
def main(args: Array[String]) {
val x = "abc1.txt"

val conf = new SparkConf().setAppName("HelloWordSpark")
val sc = new SparkContext(conf)
val y = sc.textFile(x).cache() # Le cache est utiliser généralement pour mettre les donnée
# en cache et les utiliser aprés.
val count = y.flatMap(line => line.split(" "))
                .map(word => (word, 1)) # Il va compter la valeur de chaque mote grace a la fun map
                .reducebykey(_ + _)

counts.saveAsFile("Sparkout" + java.util.UUID.randomUUID.toString)
sc.stop()
}
}


CREATE TABLE IF NOT EXISTS accountscountry(
    country_code VARCHAR PRIMARY KEY
)