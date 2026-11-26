import { registerRoot, Composition } from 'remotion';
import React from 'react';
import { Clip8c } from './Clip8c';
import t from './timing_c8c.json';

const FPS = 30;
const Root = () => (<>
  <Composition id="Clip8c" component={Clip8c} durationInFrames={Math.ceil(t.total * FPS)} fps={FPS} width={1920} height={1080} />
</>);
registerRoot(Root);
