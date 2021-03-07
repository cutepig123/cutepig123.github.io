---
toc: true
---

Composition over inheritance



# Definition

Composition over inheritance: is the principle that classes should achieve [polymorphic](https://en.wikipedia.org/wiki/Polymorphism_(computer_science)) behavior and [code reuse](https://en.wikipedia.org/wiki/Code_reuse) by their [composition](https://en.wikipedia.org/wiki/Object_composition)  rather than [inheritance](https://en.wikipedia.org/wiki/Inheritance_(computer_science)) from a base or parent class.



Composition : containing instances of other classes that implement the desired functionality



mixin:  a [class](https://en.wikipedia.org/wiki/Class_(computer_science)) that contains methods for use by other classes without having to be the parent class of those other classes. Mixins are sometimes described as being "included" rather than "inherited".







# Why

- To favor composition over inheritance is a design principle that gives the design higher flexibility
- Composition also provides a more stable business domain in the long term as it is less prone to the quirks of the family members
- 



# Drawbacks

- methods being provided by individual components may have to be implemented in the derived type, even if they are only [forwarding methods](https://en.wikipedia.org/wiki/Forwarding_(object-oriented_programming)) 
- 

## Avoiding Drawbacks

This drawback can be avoided by using [traits](https://en.wikipedia.org/wiki/Traits_(computer_science)), [mixins](https://en.wikipedia.org/wiki/Mixin), *(type)* [embedding](https://en.wikipedia.org/wiki/Embedding), or [protocol](https://en.wikipedia.org/wiki/Protocol_(object-oriented_programming)) extensions.

Some languages provide specific means to mitigate this:

- [Raku](https://en.wikipedia.org/wiki/Raku_(programming_language)) provides a `handles` keyword to facilitate method forwarding.
- [Java](https://en.wikipedia.org/wiki/Java_(programming_language)) provides Project Lombok[[5\]](https://en.wikipedia.org/wiki/Composition_over_inheritance#cite_note-5) which allows delegation to be implemented using a single @Delegate annotation on the field, instead of copying and maintaining the names and types of all the methods from the delegated field.[[6\]](https://en.wikipedia.org/wiki/Composition_over_inheritance#cite_note-6)
- [Swift](https://en.wikipedia.org/wiki/Swift_(programming_language)) extensions can be used to define a default implementation of a protocol on the protocol itself, rather than within an individual type's implementation.[[7\]](https://en.wikipedia.org/wiki/Composition_over_inheritance#cite_note-7)
- [Kotlin](https://en.wikipedia.org/wiki/Kotlin_(programming_language)) includes the delegation pattern in the language syntax.[[8\]](https://en.wikipedia.org/wiki/Composition_over_inheritance#cite_note-8)
- [Go](https://en.wikipedia.org/wiki/Go_(programming_language)) type embedding avoids the need for forwarding methods.[[9\]](https://en.wikipedia.org/wiki/Composition_over_inheritance#cite_note-9)
- [D](https://en.wikipedia.org/wiki/D_(programming_language)) provides an explicit "alias this" declaration within a type can forward into it every method and member of another contained type. [[10\]](https://en.wikipedia.org/wiki/Composition_over_inheritance#cite_note-10)



# ref

- https://en.wikipedia.org/wiki/Composition_over_inheritance
- https://en.wikipedia.org/wiki/Mixin
- 