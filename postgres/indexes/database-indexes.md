- primary index: an index that allows to identify a specific record. Note that to be able to identify a row, a constraint must be applied to the value to make it *unique*. 

- unique: unicity is not an index directly, it's rather a constraint. But to be successfully enforced it requires an index, which is why one is created, if it doesn't yet exist, on the combination of columns being made unique.

## Primary key vs unique index

Primary key vs unique index. What's the difference?

Some people think the distinction lies in the set of properties the standards define for them. Can allow null, mustn't allow null, etc. I don't think it's very useful to linger in those details to understand the nuances between these concepts, since you will always find some implementation that manages to deviate from the specs.

Fortunately, concepts that are central to the terminology don't change: what is "primary", what's a "key", what's "unique", and what's an "index". So let's have an explanation from first principles that, hopefully, will stick.

### Key:
A *key* is a value that can point to a related value. Like in a hashmap (aka hash table, aka dictionary, aka associative array, etc). In the case of a database table, that related value is a record. A key is a convenience, it serves as an alias to replace the actual value, a placeholder. Many such values can exhibit these placeholding properties for a single record. That is, there can be multiple keys that can be used to find a single record.

### Primary:
A thing is said to be *primary* if it comes before other similar things. A *primary key* in a database table is thus the key among other keys that is principally used to designate or locate a table record, meaning that there might be other keys that can do the job, but this one was specifically chosen as the main way to do it. It is the canonical way recognized by the database as having this property. In other words, *primary key* is just semantics for "the one value that is guaranteed to point to the record", aka its *identifier*.

### Unique:
For a key to be an ideal alias for an object, it must be associated with only that one object, otherwise (if associated with possibly more objects) it would require additional work to further narrow the selection. Given a collection of such objects that each have a key only associated to them, if you were to create a subset made only of those keys, the subset would display the property of unicity, meaning that there would be no keys in duplicate. For a database to check or enforce that each key is unique among a set of other keys, it needs to compare each new candidate key to existing keys. If a candidate key is found to collide with an existing key, it's rejected. The declaration that enables this mechanism is called the *unique constraint*. 

### Index:
To allow for an efficient unicity verification process, the database uses a structure called an *index*, where keys are sorted which allows for a speedy check of potential collision. Note, however, that the concept of "unique value" is completely divorced from the concept of "indexing". You don't *need* an index to identify unique values (you could, for example, just traverse a collection from beginning to end and watch for duplicates), but an index is usually considerably more efficient. Thus, enforcing the *unique constraint* on a column or set of columns will usually (indirectly) also create an index on those columns. In a sense, the term "unique index" is a contraction of two separate concepts into one: the unique constraint validates values and uses an index for quick lookups of existing values.

Finally, why have only a single primary key if we can use other "unique values" in similar fashion? That's because the primary key is semantically recognized by the database for its job and can therefore be treated more specially than those other unique values to maintain some *referencial integrity*. For instance, you can use them to implicitly relate records on one table to records on another tables. Although other unique values can be used similarly, the database will not be made aware of such relations and you'll have to manage them yourself and are risking all kinds of potential problems.

Relations made using primary keys are treated particularly by the database. For example, you can't just whimsically decide to change a primary key value or delete a row it points to. The database can be configured to apply some automatic actions when that happens. It can stop you from putting your relationships in an inconsistent state, or it can propagate (aka *cascade*) your changes to other related tables (i.e. update foreign keys or delete related rows). Non-primary unique values are generally not bound by such constraints. You can manipulate them freely, within the bounds of the unique constraints (e.g. you can change a user's email), without affecting referrential integrity, at least as far as the database engine is concerned.
