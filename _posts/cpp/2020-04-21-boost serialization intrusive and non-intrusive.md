---
categories: cpp
---
boost serialization

it has 2 modes: intrusive and non-intrusive



intrusive mode

```cpp
class gps_position
{
public:
	friend class boost::serialization::access;
	// When the class Archive corresponds to an output archive, the
	// & operator is defined similar to <<.  Likewise, when the class Archive
	// is a type of input archive the & operator is defined similar to >>.
	template<class Archive>
	void serialize(Archive & ar, const unsigned int version)
	{
		ar & degrees;
		ar & minutes;
		ar & seconds;
	}
	int degrees;
	int minutes;
	float seconds;
public:
	gps_position(){};
	gps_position(int d, int m, float s) :
	degrees(d), minutes(m), seconds(s)
	{}
};
```



non-intrusive mode

```cpp

namespace boost {
	namespace serialization {

		template<class Archive>
		void serialize(Archive & ar, gps_position & g, const unsigned int version)
		{
			ar & g.degrees;
			ar & g.minutes;
			ar & g.seconds;
		}

	} // namespace serialization
} // namespace boost
```

How does boost impl the 2 modes?

A: By function overloading. by parameter specialization

For intrusive mode, following template functions are called

```cpp
boost::serialization::access::serialize<boost::archive::text_oarchive,gps_position>(boost::archive::text_oarchive & ar, gps_position & t, const unsigned int file_version);
```

Note non intrusive mode serialization's priority is always higher than  intrusive mode as it is implemented in boost::serialization name space. and it is more "specific" 
