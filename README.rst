Introduction
============

This product integrates a Google Custom Search for Plone.

The default search viewlet and search page are overloaded by this product.
A configlet registered in the control panel which let you set the id of your
google custom search engine. You can also set the google custom search id via
Generic Setup in registry.xml like so:

.. code-block:: xml

    <?xml version="1.0"?>
    <registry>
      <records interface="collective.gcs.interfaces.IGcsSettings" prefix="collective.gcs">
        <value key="gcs_id">GOOGLE CUSTOM SEARCH ID</value>
      </records>
    </registry>


Originally written for Qt by Robert Niederreiter, BlueDynamics Alliance.


Credits
=======

* Robert Niederreiter, <rnix@squarewave.at>
* Johannes Raggam, <johannes@raggam.co.at>
