Troubleshooting Miro
====================

Miro, like all other complex software that runs on many different
platforms, has bugs. We work hard to find and fix bugs, but some bugs
are hard to find and some are hard to fix.

This chapter will help you know what to do when you bump into problems.

Converting media files
----------------------

### Error: Unknown encoder: libfaac

When using Miro for conversions on most GNU/Linux distributions, you
will probably encounter failures with the message:

    Unknown encoder: libfaac

Miro uses \`ffmpeg <[http://www.ffmpeg.org/](http://www.ffmpeg.org/)\>\`
for conversions. Most distributions have ffmpeg binaries that are
compiled without the `--enable-libfaac` option because of license
conflicts with libfaac.

You can figure out whether the ffmpeg on your system was compiled with
libfaac support by opening up a console and typing:

    ffmpeg

It'll print out a bunch of stuff. One of the lines will start with
"configuration:". If that line has `--enable-libfaac`, then your ffmpeg
has libfaac and will be able to encode aac. If there is no
`--enable-libfaac`, then your ffmpeg does not have libfaac and will not
be able to encode aac.

For Ubuntu, see
[http://ubuntuforums.org/showthread.php?t=1117283](http://ubuntuforums.org/showthread.php?t=1117283)

For other distributions, consult your distribution's documentation.

### Error: None and other errors

If you see this, please report a bug and attach your conversion log file
to the bug report.

FIXME - screenshot

See :ref:\`Reporting bugs <reporting-bugs\>\` for more details and tips.

Playing media files
-------------------

Occasionally, you'll run into a media file that won't play. There are
several reasons that this could happen:

1.  **The media file is corrupted.** Try playing the file with another
    media player. If it doesn't work in other media players, then it's
    probably corrupted.

2.  **The media file is in a format Miro doesn't support.** Miro can
    play media files in a variety of formats, but there are hundreds of
    codecs out there and Miro probably doesn't support the more esoteric
    ones. Try playing the file in another media player.

3.  **You're using GNU/Linux and you're missing required GStreamer
    plugins.** Check to make sure that you have the necessary GStreamer
    plugins. This is distribution-specific, so you'll have to consult
    your distribution's documentation.

If this is a perpetual problem, you can tell Miro to play all media with
an external player in the **Preferences** dialog in the **Playback**
tab.

How to request a feature enhancement
------------------------------------

Not everyone uses Miro in exactly the same way. Not everyone has the
same set of needs. Because of this, you're likely to discover
functionality you wish Miro had.

When this happens, do the following:

1.  Open up your web browser.
2.  Go to [http://bugzilla.pculture.org](http://bugzilla.pculture.org)/
    .
3.  If you don't have an account, create one.
4.  Log in.
5.  Report a bug and mark it as an enhancement request.

If you're able to, implement the feature and attach a patch to the bug.

We take all enhancement requests seriously, but it's not possible to
implement all enhancements so we tend to implement enhancements we think
are most beneficial to most of our users.

When you find a bug
-------------------

When you bump into a bug, do the following:

1.  Open up your web browser.
2.  Go to [http://bugzilla.pculture.org](http://bugzilla.pculture.org)/
    .
3.  If you don't have an account, create one.
4.  Log in.
5.  Report the bug.

When you're reporting a bug, be sure to include as much information as
you can. The more information we have, the more likely it is that we can
reproduce the issue you're having and fix it.

If you're able to, fix the problem and attach a patch to the bug with an
explanation of how the patch fixes the problem. Seriously. This helps us
a ton and greatly increase the chance your bug will be addressed.

We take all bug reports seriously, but bugs take time to work through
and if there isn't enough information in the bug report, that makes it
that much harder.

See :ref:\`Reporting bugs <reporting-bugs\>\` for more details and tips.

When Miro hiccups
-----------------

Occasionally, some part of Miro throws an exception that Miro catches
causing Miro to show you the Internal Error dialog.

![image](_static/troubleshooting_internal_error.png)
When this happens, take some time to describe what you were doing when
the problem occurred in the text box. Then click on **Submit Crash
Report**.

If you can, please check off the *Include entire program database
including all video and feed metadata with crash report* checkbox. Being
able to see the database and log files often helps us diagnose issues
quickly.
