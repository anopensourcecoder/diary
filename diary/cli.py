"""Console script for diary."""
import sys
import click
import sys, tempfile, os
import datetime
from subprocess import call

from . import __version__
from  diary.db import DB
from  diary.diary import Diary
from diary.humandate import HumanDate

# init Diary Software
d = Diary()
h=HumanDate()

@click.group()
@click.version_option()
#@click.command()
def main():
    """Welcome to Diary (console version). Some example usage:


    diary today     <- go to today diary.

    diary add       <- edit diary in nano editor.

    diary add "wow" <- Add text from terminal.

    diary prev      <- go to previous diary

    diary nextday   <- go to next day

    diary first     <- go to last diary


    ***** Also try *******

    diary setdate --help

    diary show  --help

    https://github.com/anopensourcecoder/diary/wiki

    """
    return 0



@main.command("today")
def screen_today():
    """set date to today and display the today diary content if it is added

        \b
        Example : diary today
       """
    d.set_date("")
    item = d.get_diary()
    if not item.item_content:
        click.echo( str( item.get_item_date().date() ) + " ( " + h.pretty_date( item.get_item_date() ) + " ) ")
        click.echo("Nothing is added. Add Something using 'diary add' command")
    else:
        click.echo( str( item.get_item_date().date() ) + " ( " + h.pretty_date( item.get_item_date() ) + " ) ")
        click.echo(item.get_item_content())


@main.command("nextday")
def screen_nextday():
    """set date to next day and display the content if it is added

        \b
        Example : diary today
       """
    d.set_day(1)
    item = d.get_diary()
    if not item.item_content:
        click.echo( str( item.get_item_date().date() ) + " ( " + h.pretty_date( item.get_item_date() ) + " ) ")
        click.echo("Nothing is added. Add Something using 'diary add' command")
    else:
        click.echo( str( item.get_item_date().date() ) + " ( " + h.pretty_date( item.get_item_date() ) + " ) ")
        click.echo(item.get_item_content())


@main.command("prevday")
def screen_prevday():
    """set date to previous day and display the content if it is added

        \b
        Example : diary today
       """
    d.set_day(-1)
    item = d.get_diary()
    if not item.item_content:
        click.echo( str( item.get_item_date().date() ) + " ( " + h.pretty_date( item.get_item_date() ) + " ) ")
        click.echo("Nothing is added. Add Something using 'diary add' command")
    else:
        click.echo( str( item.get_item_date().date() ) + " ( " + h.pretty_date( item.get_item_date() ) + " ) ")
        click.echo(item.get_item_content())

@main.command("prev")
def screen_prev():
    """set date to previous existing diary and display the content

        \b
        Example : diary prev
       """
    result = d.go_previous_diary()
    item = d.get_diary()
    if result:
        click.echo(str(item.get_item_date().date()) + " ( " + h.pretty_date(item.get_item_date()) + " ) ")
        click.echo(item.get_item_content())
    else:
        click.echo(str(item.get_item_date().date()) + " ( " + h.pretty_date(item.get_item_date()) + " ) ")
        click.echo( "There is not any older diary!")



@main.command("next")
def screen_next():
    """set date to next existing diary and display the content

        \b
        Example : diary next
       """
    result = d.go_next_diary()
    item = d.get_diary()
    if result:
        click.echo(str(item.get_item_date().date()) + " ( " + h.pretty_date(item.get_item_date()) + " ) ")
        click.echo(item.get_item_content())
    else:
        click.echo(str(item.get_item_date().date()) + " ( " + h.pretty_date(item.get_item_date()) + " ) ")
        click.echo("There is not any newer diary!")

@main.command("first")
def screen_first():
    """set date to first diary  and display the  content

        Example : diary first
       """
    d.go_first_diary()
    item = d.get_diary()
    if not item.item_content:
        click.echo(str(item.get_item_date().date()) + " ( " + h.pretty_date(item.get_item_date()) + " ) ")
        click.echo("Nothing is added. Add Something using 'diary add' command")
    else:
        click.echo(str(item.get_item_date().date()) + " ( " + h.pretty_date(item.get_item_date()) + " ) ")
        click.echo(item.get_item_content())

@main.command("last")
def screen_last():
    """set date to last diary and display the content

        Example : diary last
       """
    d.go_last_diary()
    item = d.get_diary()
    if not item.item_content:
        click.echo(str(item.get_item_date().date()) + " ( " + h.pretty_date(item.get_item_date()) + " ) ")
        click.echo("Nothing is added. Add Something using 'diary add' command")
    else:
        click.echo(str(item.get_item_date().date()) + " ( " + h.pretty_date(item.get_item_date()) + " ) ")
        click.echo(item.get_item_content())



@main.command("setdate")
@click.argument("date", type=str,
                default="")
def screen_setdate(date):
    """set date to today or a exact date (year-month-day)

        \b
        Example : diary set

        \b
        Example : diary set --date 2020-05-19

       """
    d.set_date(date)
    item = d.get_diary()
    if not item.item_content:
        click.echo( str( item.get_item_date().date() ) + " ( " + h.pretty_date( item.get_item_date() ) + " ) ")
        click.echo("Nothing is added. Add Something using 'diary add' command")
    else:
        click.echo( str( item.get_item_date().date() ) + " ( " + h.pretty_date( item.get_item_date() ) + " ) ")
        click.echo(item.get_item_content())



@main.command("showdate")
@click.argument("date", type=str,
                default="")
def screen_dateshow(date):
    """show selected date (year-month-day)

        \b
        Example : diary set

        \b
        Example : diary set --date 2020-05-19

       """
    item_date = d.get_date()
    if item_date is not None:
        click.echo(str(item_date.date()) + " ( " + h.pretty_date(item_date) + " ) ")
    else:
        click.echo("Something went wrong!." )



@main.command("show")
def screen_showdiary():
    """Show diary

        \b
        Example : diary show

       """
    item = d.get_diary()
    if not item.item_content:
        click.echo(item.get_item_date())
        click.echo("Nothing is added. Add Something using 'diary add' command")
    else:
        click.echo( str( item.get_item_date().date() ) + " ( " + h.pretty_date( item.get_item_date() ) + " ) ")
        click.echo( item.get_item_content())



@main.command("add")
@click.argument("content",
                default="",
                type=str)
def screen_add(content):
    """ Add text to diary for the selected date.

        \b
        Example : diary add 'Today is good day!'

        Add text using Nano editor
        \b
        Example : diary add
       """

    current_content = d.get_diary_content()

    if content !="":
        item = d.add_diary(current_content + " \n " +content)
    else:
        EDITOR = os.environ.get('EDITOR', 'nano')  # that easy!

        initial_message = current_content.encode()  # if you want to set up the file somehow

        with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
            tf.write(initial_message)
            tf.flush()
            call([EDITOR,"-I", tf.name])

            # do the parsing with `tf` using regular File operations.
            # for instance:
            tf.seek(0)
            edited_message = tf.read()

        item = d.add_diary(edited_message.decode("utf-8"))

    click.echo("Record added. Use 'diary show' to check. ")



@main.command("zz")
def screen_zz():
    """ Show Debug details """
    click.echo("----------------debug------------------")
    #click.echo( d.__str__() )
    click.echo(d.__repr__())

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
