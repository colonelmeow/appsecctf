# appseccft
<h1>CTF Anwers</h1>


<h1>Challenge 1:</h1>
Answers and Notes:
<ul>
<li>1. There are several things that can be addressed with this application. <b>CVE-2018-18074</b> can be addressed by modifying the requirements file to install <b>requests=2.22.0</b> rather than the vulnerable version. Also there are a lot of package imports in the script itself that aren't being used, and should be removed until they are.</li>
<li>2. Update the version of the alpine image being used. The application itself doesnt really do anything at this point so there is no reason not to use the latest version especially as it fixes <b>CVE-2019-8457</b> by installing a patched version of SQLite.</li>
<li>3. In the dockerfile there are a lot of things being installed that aren't being used. This needlessly increases the size of the attack surface. If you remove those packages you also prevent <b>gcc</b> and <b>binutils</b> from being installed which resolves <b>CVE-2018-12699</b> as that isn't an acceptable answer, this issue is also resolved by using the newer version of Alpine, or you could install the <b>acl</b> package, and lock down the permissions for <b>objdump</b> which is the vulnerable package, by blocking its use. setfacl user:*:rwx- objdump </li>
</ul>
As an asside I don't know if this is within scope, but this image install all sorts of things not being used. If the point is just to build a containerized test application to learn docker or something to that end, there are better images to use.

<h1>Challenge 2:</h1>
Answers and Notes:
1. To resolve this challenge I update the package releases for spring framework and jackson-databind to the latest versions then rescanned.

<h1>Challenge 3:</h1>
1. Updated the sample to use a parametized statement, rather than a dynamic statement
