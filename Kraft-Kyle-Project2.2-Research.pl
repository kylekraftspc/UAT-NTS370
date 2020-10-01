#!/usr/bin/perl
#The point of the USE command is to load in extra features from a named module. In
# this particular case, LWP is a module that is used for accessing data on the internet. 
use LWP::UserAgent;

#This module will understand HTML markup and seperate it from plain text.  
use HTML::Parse;

#Here the variable SITE is being assinged to the first element located in the ARGV array.
$site = @ARGV[0];

#Here the variable FILETYPE will be assigned to the 2nd element located in the ARGV array.
$filetype = @ARGV[1];

#This is assigning the variable SEARCHURL to a specific URL to be used when searching.
$searchurl = "http://www.google.com/search?hl=en&q=site%3A$site+filetype%3A$filetype";

$useragent = new LWP::UserAgent;
$useragent->agent('Mozilla/4.0 (compatible; MSIE 5.0; Windows 95)');

$request = HTTP::Request->new('GET');
$request->url($searchurl);
$response = $useragent->request($request);
$body = $response->content;

$parsed = HTML::Parse::parse_html($body);
for (@{ $parsed->extract_links(qw(a)) }) {
  ($link) = @$_;
  if ($link =~ m/url/){
     print $link . "\n";
     }
} 


