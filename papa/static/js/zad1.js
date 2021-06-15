function zad1(a,b) {
    return a + b
}

console.log(zad1(1,2))

function zad2(a){
    return a*4
}

console.log(zad2(1))

function zad3(a,b,c){
    return (a+b+c)/3
}

console.log(zad3(1,2,3))

function zad4(){
    return 7
}

console.log(zad4())

function zad5(a){
    return a%5
}

console.log(zad5(16))

function zad6(a,b){
    d = {}
    d['a'] = a
    d['b'] = b
    d['c'] = a+b
    return d

}

console.log(zad6(1,2))

function zad7(a) {
    return (a.indexOf(8) != -1 || a.indexOf(4) != -1)

}

console.log(zad7([1,2,3,4,5,6,7]))

function zad8(a,b){
    return a[1]/b[0]
}
console.log(zad8([1,2,3],[12,45]))

function zad9(a){
    return a.replaceAll(' ','privet')
}

console.log(zad9('asad s ddf g'))

function zad10(a){
    b = a.split(' ')
    return b[1]
}

console.log(zad10('123 ff tyh'))
