---
title: 'AdvancedProgramming: JSON'
customTheme : 'leagueFabio'
highlightTheme: 'monokai' 
transition: 'slide'
transitionSpeed: 'fast'
center: true
slideNumber: true
navigationMode: 'linear'
controls: false
width: 1920
height: 1080
defaultTiming: 52

---

## Advanced Programming: 

# JSON

---

## Why are we here?

 * Write a JSON successor that is better than anything

--

## Why are we here?

 * ~~Write a JSON successor that is better than anything~~

--

## Why are we here?

* We want to train programming{.fragment}
* We want a realistic but feasible problem to practice on{.fragment}
* We want a common problem{.fragment} 
  * We want to compare notes{.fragment}

--

This course requires active contribution both in the workshop parts and on homework (~1 day per week). 
If you sign up for this course please make sure that you can commit to that as other participants will depend on it.

---

## The Task

Create a more space efficient JSON

* The API should allow basic usage examples e.g. like [these](https://www.programiz.com/python-programming/json){.fragment}
* The output of the serialization should be shorter (or at least not longer) than the JSON output{.fragment}

--

```
import json

person_dict = {'name': 'Bob', 'age': 12, 'children': None }
person_json = json.dumps(person_dict)

# Output: {"name": "Bob", "age": 12, "children": null}
print(person_json)
```

--

```
import our_better_json

person_dict = {'name': 'Bob', 'age': 12, 'children': None }
person_json = our_better_json.dumps(person_dict)

# Output: S4nameS3BobS3ageI12S8childrenN
print(person_json) 
```

--

### Acceptance criteria

* Supported types:
  * Dict
  * Array
  * String
  * Number (Int and float)
  * Bool
  * None
* Round trip works:{.fragment}
  * String -> Python object -> String{.fragment}
  * Python object -> String -> Python Object{.fragment}

--

### Technical quality measurements

* Ratio Size: JSON string vs Our protocol{.fragment}
* Runtime speed:{.fragment} 
  * JSON Serialization{.fragment}
  * JSON Deserialization{.fragment}

---

## Learning Resources

* [Python JSON Documentatin](https://docs.python.org/3/library/json.html)
* Existing Formats:
  * Binary JSON [BSON](https://en.wikipedia.org/wiki/BSON), [from MongoDB](https://www.mongodb.com/basics/bson)
  * Concise Binary Object Representation [(CBOR)](https://www.rfc-editor.org/rfc/rfc8949.html)
  * MessagePack (a precursor to CBOR) [Spec](https://github.com/msgpack/msgpack/blob/master/spec.md)
  * [UBJSON](https://ubjson.org/) and [BJData](https://github.com/NeuroJSON/bjdata/blob/master/Binary_JData_Specification.md)


--

## Learning Resources - Test Data

Get some data to test with:

 * [NLohmann JSON Testdata](https://github.com/nlohmann/json_test_data/tree/master)
 * [JSONPlaceholder](https://jsonplaceholder.typicode.com/)
 * [Awsome Datasets](https://awesomeopensource.com/project/jdorfman/awesome-json-datasets) Has some stale links


---

## Working Plan:

Start With (till next session/ 2 Weeks):

* Tests{.fragments}
* Benchmarks{.fragments}
* Sketch out Serialization{.fragments}  
  * (as far as it will go){.fragments}

--

### Next session

check in

* Answer questions
* Remove Blockers
* (Align on API)

--

##  Working Plan:

In two Sessions (3rd April - 6 Weeks)

* The full thing

--

### The April session

"Post Mortem"/Lessons Learned

We will then swap projects, and do some refactorings on each others code

--

### Last Session

More lessons Learned


---

## Thank You

---