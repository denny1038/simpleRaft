
from .voter import Voter

class Candidate( Voter ):

	def set_server( self, server ):
		self._server, server

		self._start_election()

	def _start_election( self ):
		self._server._currentTerm += 1
		election = ElectionMessage( self._server._name, 
					    None, 
					    self._server._currentTerm, 
					    { 
						"lastLogIndex": self._server._lastLogIndex,
						"lastLogTerm": self._server._lastLogValue })

		self._server.send_message( election )
		self._last_vote = self._name
